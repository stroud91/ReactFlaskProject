from .db import db, environment, SCHEMA, add_prefix_for_prod

class BusinessImage(db.Model):
    __tablename__ = 'business_images'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    business_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod("businesses.id")), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    image_preview = db.Column(db.Boolean(), nullable=False)
    # created_at = db.Column(db.DateTime(), nullable=False)
    # updated_at = db.Column(db.DateTime(), nullable=False)

    business = db.relationship("Business", back_populates='images')
    user = db.relationship("User", back_populates='business_image')

    def to_dict(self):
        return {
            'id': self.id,
            'business_id': self.business_id,
            'user_id': self.user_id,
            'image_url': self.image_url,
            'image_preview': self.image_preview,
            # 'created_at': self.created_at,
            # 'updated_at': self.updated_at
        }
