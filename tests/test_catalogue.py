import pytest
import json
from app import app, db
from models import Catalogue

@pytest.fixture(scope='module')
def test_client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_get_catalogues_empty(test_client):
    """Test GET /catalogues when there are no catalogues"""
    response = test_client.get('/catalogues')
    assert response.status_code == 200
    assert json.loads(response.data) == []
