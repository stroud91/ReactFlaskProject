from flask import Blueprint, jsonify
from ..models import Business, Review

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
    # review_data = [review.to_dict() for review in reviews]

    ratings = [review.rating for review in reviews]
    avg_rating = sum(ratings) / len(ratings) if ratings else 0
    business_dict['avg_rating'] = round(avg_rating, 2)

    business_dict['category'] = business.category.name if business.category else None

    # images = business.images
    # image_data = [image.to_dict() for image in images]

    # business_dict['reviews'] = review_data
    # business_dict['images'] = image_data

    return jsonify(business_dict)


#error
