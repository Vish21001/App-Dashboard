from flask import Blueprint, request, jsonify
from models import db, Review

reviews_bp = Blueprint('reviews', __name__)

# Add review
@reviews_bp.route('/', methods=['POST'])
def add_review():
    data = request.json
    review = Review(
        user_id=data['user_id'],
        app_id=data['app_id'],
        rating=data['rating'],
        comment=data.get('comment', '')
    )
    db.session.add(review)
    db.session.commit()
    return jsonify({'message': 'Review added successfully'})
