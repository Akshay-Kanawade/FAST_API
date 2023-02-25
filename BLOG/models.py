from .database import Base
from sqlalchemy import Row, Column, Integer, String

class Blog(Base):
    
    __tablename__ = 'blogs'
    
    Id  :Column(Integer, primary_key = True, index=True)
    Title : Column(String)
    Body : Column(String)