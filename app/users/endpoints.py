from fastapi import APIRouter
from fastapi import HTTPException
from starlette import status

from app.users.views import create_new_user
from app.users.views import find_user_by_email
from app.users.views import validate_passwords

# from app.users.models import User
from app.users.schemas import UserCreate
from app.helpers.db_dependency import db_dependency


router = APIRouter()


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register(db: db_dependency, user_request: UserCreate):
    """
    Register a new user
    """
    email, password_1, password_2 = user_request.email, user_request.password_1, user_request.password_2
    email_clean = email.strip().lower()
    # validate passwords
    if not validate_passwords(password_1, password_2):
        raise HTTPException(status_code=400, detail='Passwords do not match')
    # check if user exists
    user = find_user_by_email(db, email_clean)
    if user:
        raise HTTPException(status_code=400, detail='User already exists')
    create_new_user(db, email_clean, password_1)
    return {'message': 'User registered'}


@router.post('/login')
def login():
    return {'message': 'User logged in'}
