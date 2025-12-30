from flask import Blueprint, request, jsonify
from models import db, App

apps_bp = Blueprint('apps', __name__)

# Get all apps
@apps_bp.route('/', methods=['GET'])
def get_apps():
    apps = App.query.all()
    return jsonify([{
        'id': app.id,
        'name': app.name,
        'category': app.category,
        'downloads': app.downloads,
        'rating': app.rating,
        'price': app.price
    } for app in apps])

# Add a new app
@apps_bp.route('/', methods=['POST'])
def add_app():
    data = request.json
    new_app = App(
        name=data['name'],
        category=data['category'],
        subcategory=data.get('subcategory'),
        developer_name=data.get('developer_name'),
        downloads=data.get('downloads', 0),
        rating=data.get('rating', 0.0),
        price=data.get('price', 0.0)
    )
    db.session.add(new_app)
    db.session.commit()
    return jsonify({'message': 'App added successfully'}), 201
