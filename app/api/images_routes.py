from flask import Blueprint, jsonify, redirect, render_template, request
from ..models import BusinessImage, db, Business
from flask_login import current_user, login_required
from ..forms import NewImage
import datetime

images_routes = Blueprint('business', __name__)


# Get all Images by Business
@images_routes.route('/<int:id>/images')
def images(id):
    images = BusinessImage.query.filter_by(business_id=id)
    
    # find business
    business = Business.query.get(id)
    if not business:
        return jsonify({"error": "Business not found"}), 404
    
    images_data = []

    for image in images:
        img_dict = image.to_dict()

        images_data.append(img_dict)
    return jsonify(images_data)

@images_routes.route('/<int:id>/images', methods=["POST"])
@login_required
def images_post(id):
    form = NewImage(request.form)

    # find business
    business = Business.query.get(id)
    if not business:
        return jsonify({"error": "Business not found"}), 404
    
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        data = form.data
        new_image = BusinessImage(image_url=data["image_url"],
                                  image_preview=data["image_preview"],
                                  business_id=id,
                                  user_id=current_user.id,
                                  created_at=datetime.datetime.now(),
                                  updated_at=datetime.datetime.now())
        db.session.add(new_image)
        db.session.commit()
        return jsonify(new_image.to_dict()), 201
    else:
        return jsonify({"errors": form.errors}), 400


@images_routes.route('/images/<int:id>', methods=["DELETE"])
def images_delete(id):
    image = BusinessImage.query.get(id)
    # find image
    if not image:
        return jsonify({"error": "Image not found"}), 404
    db.session.delete(image)
    db.session.commit()
    return "Successfully deleted"
