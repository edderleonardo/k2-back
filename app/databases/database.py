from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SQLALCHEMY_DATABASE_URL = 'postgresql://vwiyrcvi:EGoELlHoMmbh9oxhdYdtPZ6OP5ZdFY8E@fanny.db.elephantsql.com/vwiyrcvi'

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
