from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config.settings import DATABASE_URI

engine = create_engine(DATABASE_URI)

DBSession = sessionmaker(bind=engine)

Base = declarative_base()
