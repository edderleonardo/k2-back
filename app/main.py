from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.users import models as user_models
from app.users.endpoints import router as user_router
from app.databases.database import engine


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=['*'], allow_headers=['*']
)

user_models.Base.metadata.create_all(bind=engine)

app.include_router(user_router)
