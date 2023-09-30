from flask import Blueprint, jsonify, redirect, render_template, request
from ..models import BusinessImage, db, Business
from flask_login import current_user, login_required
from ..forms import NewImage
from datetime import datetime

images_routes = Blueprint('business', __name__)

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}

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
    # return jsonify(images_data)
    return {"images": {image.id: image.to_dict() for image in images}}



@images_routes.route('/<int:id>/images', methods=["POST"])
@login_required
def images_post(id):
    form = NewImage()
    # find business
    business = Business.query.get(id)
    if not business:
        return jsonify({"error": "Business not found"}), 404
    
    form['csrf_token'].data = request.cookies['csrf_token']
    # print(form.data)
    if form.validate_on_submit():
        data = form.data
        
        # print(data)
        # Update 
        if data['image_preview'] == "true":
            data['image_preview'] = True
        else:
            data['image_preview'] = False

        if data["image_preview"] == True:
            images = db.session.query(BusinessImage).filter(BusinessImage.business_id == id).all()
            for image in images:
                image.image_preview=False
                image.updated_at=datetime.utcnow()

        new_image = BusinessImage(image_url=data["image_url"],
                                  image_preview=data['image_preview'],
                                  business_id=id,
                                  user_id=current_user.id,
                                  created_at=datetime.utcnow(),
                                  updated_at=datetime.utcnow())
        db.session.add(new_image)
        db.session.commit()

        return new_image.to_dict(), 201
    else:
        return jsonify({"errors": form.errors}), 400


@images_routes.route('/images/<int:id>', methods=["DELETE"])
@login_required
def images_delete(id):
    image = BusinessImage.query.get(id)
    if not image:
        return jsonify({"error": "Image not found"}), 404
    business = Business.query.get(image.business_id)
    # print(business.owner_id)

# confirm user
# if the current owner is not the business owner
# owner of image deletes their own image - pass
#owner of the business deletes their own image - pass
#random person deleting image - pass
    if current_user.id != image.user_id and business.owner_id != current_user.id:
        return jsonify({"error": "Unauthorized to delete this image"}), 403
    

    db.session.delete(image)
    db.session.commit()

    last_img = BusinessImage.query.filter(
                BusinessImage.business_id == image.business_id).order_by(BusinessImage.created_at.desc()).first()

    if last_img:
            last_img.image_preview=True
            last_img.updated_at=datetime.utcnow()

            db.session.commit()

    return "Successfully deleted"


# AWS Routes

# @images_routes.route("/<int:id>/images/aws", methods=["GET","POST"])
# @login_required
# def upload_image(id):
#     form = NewImage()

#     if request.method == "POST":
#         if form.validate_on_submit():

#             image = form.data["image_url"]
#             image.filename = get_unique_filename(image.filename)
#             upload = upload_file_to_s3(image)
#             print(upload)

#             if "url" not in upload:
#             # if the dictionary doesn't have a url key
#             # it means that there was an error when you tried to upload
#             # so you send back that error message (and you printed it above)
#                 return render_template("post_form.html", form=form, errors=[upload])

#             url = upload["url"]


#             new_image = BusinessImage(image_url = url,
#                                       image_preview=False,
#                                       business_id=id,
#                                       user_id=current_user.id,
#                                       created_at=datetime.utcnow(),
#                                       updated_at=datetime.utcnow())
#             db.session.add(new_image)
#             db.session.commit()
#             return redirect(f'/business/{id}/images')

#     if form.errors:
#         print(form.errors)
#         return render_template("post_form.html", form=form, errors=form.errors)
    
#     files = BusinessImage.query.all()

#     return render_template("post_form.html", files=files, errors=None)