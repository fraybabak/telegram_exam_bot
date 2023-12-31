from sqlalchemy import Column, Integer, Boolean, ForeignKey, Text
from database import Base, session

class QuestionModel(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    question = Column(Text, index=True, unique=True)
    answer = Column(Boolean)
    rating = Column(Integer)
    context_id = Column(Integer, ForeignKey('context.id'), nullable=True)

