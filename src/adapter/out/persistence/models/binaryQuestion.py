from sqlalchemy import Column, Integer, Boolean, ForeignKey, Text
from database import Base, session

class BinaryQuestionModel(Base):
    __tablename__ = 'binary_questions'
    id = Column(Integer, primary_key=True)
    question = Column(Text, index=True, unique=True)
    answer = Column(Boolean)
    rating = Column(Integer)
    context_id = Column(Integer, ForeignKey('context.id'), nullable=True)

Base.metadata.create_all(session.bind)