from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Review
from sqlalchemy import or_
from ..models import db, Review, Business
from..forms.review_form import ReviewForm


review_routes = Blueprint('review', __name__)

@review_routes.route('')
def all_reviews():
    reviews = Review.query.all()
    all_reviews = []
    for review in reviews:
        print(review.to_dict())
        all_reviews.append(review.to_dict())
        #print("Hi there")
        #print(all_reviews)
    return {"Reviews": all_reviews}



@review_routes.route('/current')
@login_required
def get_user_reviews():
    """
    Retrieve reviews of the current logged-in user.
    """
    user_reviews = []
    for review in current_user.reviews:
        user_reviews.append(review.to_dict())
    
    return jsonify({"User_reviews": user_reviews})


@review_routes.route('/<int:id>/reviews')
def single_business_reviews(id):
    business = Business.query.get(id)
    reviews = Review.query.filter_by(business_id=id).all()
    
    # Create a list of review dictionaries
    review_list = [review.to_dict() for review in reviews]
    
    return {"restaurant_reviews": review_list}

@review_routes.route('/<int:id>/reviews', methods=['POST'])
@login_required
def create_review(id):
    form = ReviewForm()
    # Check if the restaurant exists
    business = Business.query.get(id)
    form['csrf_token'].data = request.cookies['csrf_token']
    #print(business)
    if not business:
        return {"error": "Business not found"}
    #query reviews by user id, if there are any, throw err msg saying user can't post more than once
    user_reviews = Review.query.filter_by(business_id = id).filter_by(user_id = current_user.id).all()

    if user_reviews:
        return {"error": "Can't post more than one review per business!"}

    # Create a new review using the form data
    if form.validate():
        new_review = Review(
            review_body=form.review_body.data,
            rating=form.rating.data,
            business_id=id,
            user_id=current_user.id
        )

        # Add and commit the new review to the database
        db.session.add(new_review)
        db.session.commit()

        return {"review": new_review.to_dict()}

    # If form validation fails, return errors
    return {"errors": form.errors}


@review_routes.route('/<int:id>', methods=["PUT"])
@login_required
def edit_review(id):
    # Check if the review exists
    review = Review.query.get(id)
    if not review:
        return {"error": "Review not found"}, 404

    # Check if the logged-in user is the owner of the review
    if review.user_id != current_user.id:
        return {"error": "You are not authorized to edit this review"}, 403

    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate():
        # Update the review with the new data
        review.review_body = form.review_body.data
        review.rating = form.rating.data

        # Commit the changes to the database
        db.session.commit()

        return {"review": review.to_dict()}, 200

    return {"errors": form.errors}, 400


@review_routes.route('/<int:id>', methods=["DELETE"])
@login_required
def delete_review(id):
    review = Review.query.get(id)

    if not review:
        return {"error": "Review not found"}, 404

    if review.user_id != current_user.id:
        return ({"error": "Forbidden"}), 403

    db.session.delete(review)
    db.session.commit()

    return {"Message": "Successfully deleted"}, 200