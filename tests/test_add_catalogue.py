# # tests/test_add_catalogue.py
# import pytest
# from app import create_app, db
# from models import AddCatalogue

# @pytest.fixture
# def client():
#     app = create_app('testing')
#     with app.test_client() as client:
#         with app.app_context():
#             db.create_all()
#         yield client
#         with app.app_context():
#             db.drop_all()

# @pytest.fixture
# def add_catalogue(client):
#     catalogue = AddCatalogue(
#         image_url='https://example.com/image.jpg',
#         brand='Toyota',
#         model='Corolla',
#         category='Sedan',
#         price=2500000,
#         rating=4.5,
#         release_date='2024-01-01'
#     )
#     db.session.add(catalogue)
#     db.session.commit()
#     return catalogue

# def test_get_add_catalogue(client, add_catalogue):
#     response = client.get(f'/catalogues/{add_catalogue.id}')
#     assert response.status_code == 200
#     data = response.get_json()
#     assert data['id'] == add_catalogue.id
#     assert data['brand'] == add_catalogue.brand

# def test_post_add_catalogue(client):
#     response = client.post('/catalogues', json={
#         'image_url': 'https://example.com/image.jpg',
#         'brand': 'Toyota',
#         'model': 'Corolla',
#         'category': 'Sedan',
#         'price': 2500000,
#         'rating': 4.5,
#         'release_date': '2024-01-01'
#     })
#     assert response.status_code == 201
#     data = response.get_json()
#     assert 'id' in data
#     assert data['brand'] == 'Toyota'
