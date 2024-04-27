from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_register_validate_password():
    response = client.post(
        '/register', json={'email': 'user@gmail.com', 'password_1': 'password', 'password_2': 'password1'}
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Passwords do not match'}


@patch('app.users.endpoints.find_user_by_email')
def test_user_exists(find_user_by_email):
    find_user_by_email.return_value = {'email': 'userexists@gmail.com', 'password': 'hashed_password'}

    response = client.post(
        '/register', json={'email': 'userexists@gmail.com', 'password_1': 'password', 'password_2': 'password'}
    )
    assert response.status_code == 400


def create_new_user(db, email, password):
    """
    Create a new user, with the given email and password, the password is hashed before saving
    """
    response = client.post(
        '/register', json={'email': 'edderleonardo@gmail.com', 'password_1': 'secret1', 'password_2': 'secret1'}
    )

    assert response.status_code == 201
    assert response.json() == {'message': 'User registered'}
