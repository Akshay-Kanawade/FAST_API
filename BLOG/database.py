from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"





Engine = create_engine(SQLALCHEMY_DATABASE_URL, 
            connect_args = {"check_same_thread":False})
Session = sessionmaker(bind=Engine)
Session.configure(bind=Engine, autocommit= False , autoflush =  False,)

Base = declarative_base()

