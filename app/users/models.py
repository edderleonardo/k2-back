import uuid
from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import String

from app.databases.database import Base


class User(Base):
    __tablename__ = 'users'

    uuid = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(String, default=datetime.now())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.uuid = str(uuid.uuid4())
        self.created_at = datetime.now()
