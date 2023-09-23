from flask import Blueprint, jsonify, request
from ..models import Business, Review, db , Category
from ..forms.bussiness_form import BusinessForm
from datetime import datetime
from flask_login import current_user, login_user, logout_user, login_required


business_routes = Blueprint('businesses', __name__)


# Get all Business
@business_routes.route('/')
def businesses():
    businesses = Business.query.all()
    businesses_data = []

    for business in businesses:
        business_dict = business.to_dict()

        reviews = business.reviews
        ratings = [review.rating for review in reviews]

        avg_rating = sum(ratings) / len(ratings) if ratings else 0
        business_dict['avg_rating'] = round(avg_rating, 2)

        business_dict['category'] = business.category.name if business.category else None

        businesses_data.append(business_dict)

    return jsonify(businesses_data)


@business_routes.route('/<int:id>')
def business_detail(id):
    business = Business.query.get_or_404(id)
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
    form = BusinessForm(request.form)

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

        return jsonify(business.to_dict()), 201
    else:
        return jsonify({"errors": form.errors}), 400


@business_routes.route('/<int:b_id>/edit', methods=['POST'])
@login_required
def edit_business(b_id):
    form = BusinessForm(request.form)

    business = Business.query.get(b_id)

    form['csrf_token'].data = request.cookies['csrf_token']

    if not business:
        return jsonify({"error": "Business not found"}), 404

    if current_user.id != business.owner_id:
        return jsonify({"error": "Unauthorized to edit this business"}), 403

    if form.validate():

        attributes_to_update = ['name', 'address', 'city', 'state', 'zip_code', 'phone_number', 'category_id', 'website', 'about', 'type']
        for attr in attributes_to_update:
            if hasattr(form, attr):
                setattr(business, attr, getattr(form, attr).data)

        business.updated_at = datetime.utcnow()
        db.session.commit()


        temp = db.session.query(Category).filter(Category.id == business.category_id).first()
        if temp:
            b_dict = business.to_dict()
            b_dict['category'] = {'name': temp.name}
        else:
            b_dict = business.to_dict()

        return jsonify(b_dict), 200
    else:
        return jsonify({"errors": form.errors}), 400




@business_routes.route('/<int:b_id>/delete', methods=['DELETE'])
def delete_business(b_id):
    business = Business.query.get(b_id)

    if not business:
        return jsonify({"error": "Business not found"}), 404

    if current_user.id != business.owner_id:
        return jsonify({"error": "Unauthorized to delete this business"}), 403

    temp = business.to_dict()

    try:
        for review in business.reviews:
            db.session.delete(review)

        db.session.delete(business)
        db.session.commit()


        response = {
            "message": "Business successfully deleted.",
            "business": temp
        }

        return jsonify(response)

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred while deleting the business", "message": str(e)}), 500
