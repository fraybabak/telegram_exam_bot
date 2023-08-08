from sqlalchemy import Column, Integer, String
from database import Base, session

class ContextModel(Base):
    __tablename__ = 'context'
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True, unique=True)
    description = Column(String, index=True, unique=True)
    


