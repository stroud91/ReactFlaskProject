from .db import db

class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=40), nullable=False)

    businesses = db.relationship("Business", backref="category")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
