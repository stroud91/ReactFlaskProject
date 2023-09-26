from flask import Blueprint, jsonify, request
from ..models import Business, Review, db , Category

categories_routes = Blueprint('categories', __name__)



@categories_routes.route('/')
def get_categories():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])
