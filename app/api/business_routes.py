from flask import Blueprint, jsonify, request
from ..models import Business, Review, db , Category, BusinessImage
from ..forms.bussiness_form import BusinessForm
from ..forms.search_form import SearchForm
from datetime import datetime
from ..config import Config
from flask_login import current_user, login_user, logout_user, login_required
from .auth_routes import validation_errors_to_error_messages
import requests
business_routes = Blueprint('businesses', __name__)





def get_coordinates(address, city, state, zip_code):
    full_address = f"{address}, {city}, {state}, {zip_code}"
    api_key = Config.GOOGLE_MAPS_API_KEY

    response = requests.get(
        'https://maps.googleapis.com/maps/api/geocode/json',
        params={'address': full_address, 'key': api_key}
    )

    if response.status_code == 200:
        content = response.json()
        
        if content['status'] == 'OK':
            latitude = content['results'][0]['geometry']['location']['lat']
            longitude = content['results'][0]['geometry']['location']['lng']
            return latitude, longitude
        else:
            return None, None
    else:
        return None, None


#Search business by name
@business_routes.route('/search', methods=['POST'])
def search_business():
    form = SearchForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    business_list =[]

    if form.validate():
        searchTerm = form.search.data
        businesses = Business.query.filter(Business.name.ilike(f'%{searchTerm}%')).all()
        business_list = []
        for business in businesses:
            business_dict = business.to_dict()
            reviews = business.reviews
            ratings = [review.rating for review in reviews]
            imgs_list = []
            images = BusinessImage.query.filter_by(business_id = business.id).all()
            for image in images:
                img_dic = image.to_dict()
                imgs_list.append(img_dic)

            avg_rating = sum(ratings) / len(ratings) if ratings else 0
            business_dict['avg_rating'] = round(avg_rating, 2)
            business_dict['images'] = imgs_list
            business_dict['category'] = business.category.name if business.category else None


            business_list.append(business_dict)
    return {"queried businesses": business_list}



# Get all Business
@business_routes.route('/')
def businesses():
    businesses = Business.query.all()
    businesses_data = []

    for business in businesses:
        business_dict = business.to_dict()

        reviews = business.reviews
        ratings = [review.rating for review in reviews]
        imgs_list = []
        images = business.images
        for image in images:
            img_dic = image.to_dict()
            imgs_list.append(img_dic)

        avg_rating = sum(ratings) / len(ratings) if ratings else 0
        business_dict['avg_rating'] = round(avg_rating, 2)

        business_dict['images'] = imgs_list

        business_dict['category'] = business.category.name if business.category else None

        businesses_data.append(business_dict)

    return jsonify(businesses_data)


@business_routes.route('/<int:id>')
def business_detail(id):

    business = Business.query.get_or_404(id)


    if business.latitude is None or business.longitude is None:
        latitude, longitude = get_coordinates(business.address, business.city, business.state, business.zip_code)
        if latitude and longitude:
            business.latitude = latitude
            business.longitude = longitude
            db.session.commit()

    business_dict = business.to_dict()

    reviews = business.reviews
    review_data = [review.to_dict() for review in reviews]

    ratings = [review.rating for review in reviews]
    avg_rating = sum(ratings) / len(ratings) if ratings else 0
    business_dict['avg_rating'] = round(avg_rating, 2)

    business_dict['category'] = business.category.name if business.category else None

    images = business.images
    image_data = [image.to_dict() for image in images]

    business_dict['reviews'] = review_data
    business_dict['images'] = image_data


    return jsonify(business_dict)





@business_routes.route('/new-business', methods=['POST'])
@login_required
def add_business():
    form = BusinessForm()

    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        business = Business(
            name=form.name.data,
            address=form.address.data,
            city=form.city.data,
            state=form.state.data,
            zip_code=form.zip_code.data,
            phone_number=form.phone_number.data,
            category_id=form.category_id.data,
            owner_id=form.owner_id.data,
            website=form.website.data,
            about=form.about.data,
            type=form.type.data,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        db.session.add(business)
        db.session.commit()
        business_to_dict = business.to_dict()
        business_to_dict["images"]=[]
        return business_to_dict
    else:
        return {"errors": validation_errors_to_error_messages(form.errors)}


@business_routes.route('/<int:b_id>/edit', methods=['POST'])
@login_required
def edit_business(b_id):
    form = BusinessForm()
    business = Business.query.get(b_id)
    form['csrf_token'].data = request.cookies['csrf_token']

    if not business:
        return jsonify({"error": "Business not found"}), 404

    if current_user.id != business.owner_id:
        return jsonify({"error": "Unauthorized to edit this business"}), 403

    if form.validate_on_submit():
        address_fields_updated = any(
            getattr(form, field).data != getattr(business, field)
            for field in ['address', 'city', 'state', 'zip_code']
        )

        if address_fields_updated:
            latitude, longitude = get_coordinates(
                form.address.data, form.city.data, form.state.data, form.zip_code.data
            )

            if not latitude or not longitude:
                return jsonify({"errors": ["Geocoding failed, please check the address provided."]}), 422

            business.latitude = latitude
            business.longitude = longitude

        for attr in ['name', 'address', 'city', 'state', 'zip_code', 'phone_number', 'category_id', 'website', 'about', 'type']:
            setattr(business, attr, getattr(form, attr).data)

        business.updated_at = datetime.utcnow()
        db.session.commit()
        return jsonify(business.to_dict())
    else:
        return jsonify({"errors": validation_errors_to_error_messages(form.errors)})




@business_routes.route('/<int:b_id>/delete', methods=['DELETE'])
def delete_business(b_id):
    business = Business.query.get(b_id)
    images = BusinessImage.query.filter_by(business_id = b_id).all()

    if not business:
        return jsonify({"error": "Business not found"}), 404

    if current_user.id != business.owner_id:
        return jsonify({"error": "Unauthorized to delete this business"}), 403

    temp = business.to_dict()

    try:
        for review in business.reviews:
            db.session.delete(review)
        for image in images:
            db.session.delete(image)
        db.session.delete(business)
        db.session.commit()


        response = {
            "message": "Business successfully deleted.",
            # "business": temp
        }

        return jsonify(response)

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred while deleting the business", "message": str(e)}), 500
