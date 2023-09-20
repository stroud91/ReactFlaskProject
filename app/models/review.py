from .db import db, environment, SCHEMA
from .business import Business
from .user import User

class Review(db.Model):
    __tablename__= 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer,primary_key=True,autoIncrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    business_id = db.Column(db.Integer,db.ForeignKey("businesses.id"))
    review_body = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())

    business_review  = db.relationship("Business", back_populates="reviews")
    user = db.relationship("User", back_populates= "reviews")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'business_id': self.business_id,
            'review_body': self.review_body,
            'rating': self.rating,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
