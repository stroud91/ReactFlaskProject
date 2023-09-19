from .db import db

class BusinessImage(db.Model):
    __tablename__ = 'business_image'
    
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    business_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    image_preview = db.Columb(db.Boolean(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    used = db.Column(db.Boolean(100), nullable=False)

    business = db.relationship("Business", back_populates='business_images')
    user = db.relationship("User", back_populates='business_images')