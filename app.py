from flask import Flask
from flask_restful import Api,Resource
from models import db  # Assuming models.py is in the same directory
from flask_migrate import Migrate
from resources.catalogue import CatalogueResource
from resources.news import NewsResource
from resources.users import Register, Login
from resources.add_catalogue import CatalogueAddResource
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)
# app.config.from_object(Config)  # Uncomment and adjust as needed
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dealership.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gambi:48Pm99A8?@localhost/dealership'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)  # Enable CORS for cross-origin resource sharing

# Initialize SQLAlchemy and Flask-Migrate
db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt (app)

# Initialize Flask-RESTful API
api = Api(app)

# Add RESTful resources to API
api.add_resource(CatalogueResource, '/catalogues')
api.add_resource(NewsResource, '/news')
api.add_resource(Login, '/login')
api.add_resource(Register, '/register')
# api.add_resource(CatalogueAddResource, '/add_catalogues', '/add_catalogues/<int:add_catalogue_id>')
# Add other resources as needed

if __name__ == '__main__':
    app.run(debug=True)