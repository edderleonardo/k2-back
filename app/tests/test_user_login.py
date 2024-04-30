from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app
from app.users.models import User


client = TestClient(app)


def test_user_not_exist():
    response = client.post('/login', json={'email': 'juaito@gmail.com', 'password': 'secret1'})
    assert response.status_code == 400
    assert response.json() == {'detail': 'Invalid credentials'}


@patch('app.users.endpoints.authenticate_user')
def test_user_login(authenticate_user):
    user = User(email='edderleonardo@gmail.com', hashed_password='hashed_password')
    authenticate_user.return_value = user 

    response = client.post('/login', json={'email': 'edderleonardo@gmail.com', 'password': 'secret1'})

    assert response.status_code == 200
