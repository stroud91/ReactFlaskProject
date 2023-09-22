from flask import Blueprint, jsonify
from ..models import BusinessImage

images_routes = Blueprint('business', __name__)


# Get all Business
@images_routes.route('/images')
def images():
    images = BusinessImage.query.all()
    images_data = []
    print("look here")
    print(images)

    for image in images:
        img_dict = image.to_dict()

        images_data.append(img_dict)
    
    return jsonify(images_data)


# @business_routes.route('/<int:id>')
# def business_detail(id):
#     business = Business.query.get_or_404(id)
#     business_dict = business.to_dict()

#     reviews = business.reviews
#     # review_data = [review.to_dict() for review in reviews]

#     ratings = [review.rating for review in reviews]
#     avg_rating = sum(ratings) / len(ratings) if ratings else 0
#     business_dict['avg_rating'] = round(avg_rating, 2)

#     business_dict['category'] = business.category.name if business.category else None

#     # images = business.images
#     # image_data = [image.to_dict() for image in images]

#     # business_dict['reviews'] = review_data
#     # business_dict['images'] = image_data

#     return jsonify(business_dict)


# #error
