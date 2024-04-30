from datetime import datetime
from datetime import timezone
from datetime import timedelta

from jose import JWTError
from jose import jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

from app.users.models import User


SECRET_KEY = '2b22eff87b074290a87cfa857e6fb876'
ALGORITHM = 'HS256'

bycrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def validate_passwords(password_1, password_2):
    """
    Validate that the two passwords match
    """
    return password_1 == password_2


def find_user_by_email(db, email):
    """
    Find a user by email
    """
    return db.query(User).filter(User.email == email).first()


def create_new_user(db, email, password):
    """
    Create a new user, with the given email and password, the password is hashed before saving
    """
    create_user = User(email=email, hashed_password=bycrypt_context.hash(password))
    db.add(create_user)
    db.commit()


def authenticate_user(db, email, password):
    """
    Authenticate a user by email and password
    """
    user = find_user_by_email(db, email)
    if not user:
        return False
    if not bycrypt_context.verify(password, user.hashed_password):
        return False
    return user


def generate_access_token(email, user_id, expires_delta):
    """
    Generate an access token
    """
    encode = {'sub': email, 'user_id': user_id}
    expire = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
