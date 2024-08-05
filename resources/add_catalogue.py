from flask_restful import Resource, reqparse
from models import AddCatalogue
from models import db
from datetime import datetime

add_catalogue_parser = reqparse.RequestParser()
add_catalogue_parser.add_argument('image_url', type=str, required=True, help='Image URL is required')
add_catalogue_parser.add_argument('brand', type=str, required=True, help='Brand is required')
add_catalogue_parser.add_argument('model', type=str, required=True, help='Model is required')
add_catalogue_parser.add_argument('category', type=str, required=True, help='Category is required')
add_catalogue_parser.add_argument('price', type=float, required=True, help='Price is required')
add_catalogue_parser.add_argument('rating', type=float, required=True, help='Rating is required')
add_catalogue_parser.add_argument('release_date', type=lambda x: datetime.strptime(x, '%Y-%m-%d'), required=True, help='Release date is required (YYYY-MM-DD)')

class CatalogueAddResource(Resource):
    def get(self, add_catalogue_id):
        add_catalogue = AddCatalogue.query.get_or_404(add_catalogue_id, description=f'Additional Catalogue with ID {add_catalogue_id} not found')
        return {
            'id': add_catalogue.id,
            'image_url': add_catalogue.image_url,
            'brand': add_catalogue.brand,
            'model': add_catalogue.model,
            'category': add_catalogue.category,
            'price': add_catalogue.price,
            'rating': add_catalogue.rating,
            'release_date': add_catalogue.release_date.strftime('%Y-%m-%d')
        }

    def post(self):
        # args = add_catalogue_parser.parse_args()
        add_catalogue = AddCatalogue(
            image_url=args['image_url'],
            brand=args['brand'],
            model=args['model'],
            category=args['category'],
            price=args['price'],
            rating=args['rating'],
            release_date=args['release_date']
        )
        db.session.add(add_catalogue)
        db.session.commit()
        return {
            'id': add_catalogue.id,
            'image_url': add_catalogue.image_url,
            'brand': add_catalogue.brand,
            'model': add_catalogue.model,
            'category': add_catalogue.category,
            'price': add_catalogue.price,
            'rating': add_catalogue.rating,
            'release_date': add_catalogue.release_date.strftime('%Y-%m-%d')
        }, 201