from pydantic import BaseModel


class UserBase(BaseModel):
    email: str

    class Config:
        json_schema_extra = {'example': {'email': 'user@email.com'}}


# Register new user
class UserCreate(UserBase):
    password_1: str
    password_2: str

    class Config:
        json_schema_extra = {'example': {'email': 'user@email.com', 'password_1': 'password', 'password_2': 'password'}}


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        json_schema_extra = {'example': {'access_token': 'eyJ', 'token_type': 'bearer'}}
