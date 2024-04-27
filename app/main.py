from fastapi import FastAPI

from app.users import models as user_models
from app.users.endpoints import router as user_router
from app.databases.database import engine


app = FastAPI()

user_models.Base.metadata.create_all(bind=engine)

app.include_router(user_router)
