import pytest
import json
from app import app, db
from models import User

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

def test_register_user(test_client):
    user_data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    }
    response = test_client.post('/register', json=user_data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['user']['username'] == 'testuser'

def test_register_user_existing_email(test_client):
    # First create a user
    user_data = {
        'username': 'user1',
        'email': 'testuser@example.com',  # This email is already used
        'password': 'password123'
    }
    test_client.post('/register', json=user_data)

    # Try to register again with the same email
    new_user_data = {
        'username': 'user2',
        'email': 'testuser@example.com',  # This email is already used
        'password': 'newpassword'
    }
    response = test_client.post('/register', json=new_user_data)
    assert response.status_code == 422
    data = json.loads(response.data)
    assert data['message'] == 'Email address already taken'

def test_login_user(test_client):
    user_data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    }
    test_client.post('/register', json=user_data)
    
    login_data = {
        'email': 'testuser@example.com',
        'password': 'password123'
    }
    response = test_client.post('/login', json=login_data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'Login successful'
    assert 'user' in data

def test_login_user_incorrect_credentials(test_client):
    user_data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    }
    test_client.post('/register', json=user_data)
    
    login_data = {
        'email': 'testuser@example.com',
        'password': 'wrongpassword'
    }
    response = test_client.post('/login', json=login_data)
    assert response.status_code == 403
    data = json.loads(response.data)
    assert data['message'] == 'Invalid email/password'

def test_login_user_unregistered_email(test_client):
    login_data = {
        'email': 'nonexistent@example.com',
        'password': 'password123'
    }
    response = test_client.post('/login', json=login_data)
    assert response.status_code == 403
    data = json.loads(response.data)
    assert data['message'] == 'Invalid email/password'
