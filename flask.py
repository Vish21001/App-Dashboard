from flask import Flask
from models import db
from routes.apps import apps_bp
from routes.users import users_bp
from routes.reviews import reviews_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Register Blueprints
app.register_blueprint(apps_bp, url_prefix='/apps')
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(reviews_bp, url_prefix='/reviews')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
