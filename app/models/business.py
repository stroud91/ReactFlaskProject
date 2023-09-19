from .db import db

class Business(db.Model):
    __tablename__ = "businesses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    address = db.Column(db.String(length=255), nullable=False)
    city = db.Column(db.String(length=50), nullable=False)
    state = db.Column(db.String(length=25), nullable=False)
    zip_code = db.Column(db.String(length=10), nullable=False)
    website = db.Column(db.String(length=255), nullable=False)
    about = db.Column(db.String(length=255), nullable=False)
    phone_number = db.Column(db.String(length=30), nullable=False, unique=True)
    type = db.Column(db.String(length=255), nullable=False)
    business_image = db.Column(db.String(length=255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    user = db.relationship("User", back_populates="businesses")
    reviews = db.relationship("Review", back_populates="business")
    # images = db.relationship("BusinessImage", back_populates="business")
    # category = db.relationship("Category", back_populates="businesses")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'website': self.website,
            'about': self.about,
            'phone_number': self.phone_number,
            'type': self.type,
            'business_image': self.business_image,
            'category_id': self.category_id,
            'owner_id': self.owner_id
        }
