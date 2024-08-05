from flask_restful import Resource, reqparse
from datetime import datetime
from models import Catalogue


catalogue_parser = reqparse.RequestParser()
catalogue_parser.add_argument('image_url', type=str, required=True, help='Image URL is required')
catalogue_parser.add_argument('brand', type=str, required=True, help='Brand is required')
catalogue_parser.add_argument('model', type=str, required=True, help='Model is required')
catalogue_parser.add_argument('category', type=str, required=True, help='Category is required')
catalogue_parser.add_argument('price', type=float, required=True, help='Price is required')
catalogue_parser.add_argument('rating', type=float, required=True, help='Rating is required')
catalogue_parser.add_argument('release_date', type=lambda x: datetime.strptime(x, '%Y-%m-%d'), required=True, help='Release date is required (YYYY-MM-DD)')

class CatalogueResource(Resource):
    def get(self):
       catalogues = Catalogue.query.all()
       print ([catalogue.to_dict()for catalogue in catalogues])
       return [catalogue.to_dict()for catalogue in catalogues],200

    def post(self):
        from ..app import db  # Import inside method to avoid circular import
        args = catalogue_parser.parse_args()
        catalogue = Catalogue(
            image_url=args['image_url'],
            brand=args['brand'],
            model=args['model'],
            category=args['category'],
            price=args['price'],
            rating=args['rating'],
            release_date=args['release_date']
        )
        db.session.add(catalogue)
        db.session.commit()
        return {
            'id': catalogue.id,
            'image_url': catalogue.image_url,
            'brand': catalogue.brand,
            'model': catalogue.model,
            'category': catalogue.category,
            'price': catalogue.price,
            'rating': catalogue.rating,
            'release_date': catalogue.release_date.strftime('%Y-%m-%d')
        }, 201