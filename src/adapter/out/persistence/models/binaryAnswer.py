from sqlalchemy import Column, Integer, Boolean, ForeignKey, Text
from database import Base, session





class BinaryAnswerModel(Base):
    __tablename__ = 'binary_answer'
    id = Column(Integer, primary_key=True)
    answer = Column(Boolean)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    binary_question_id = Column(Integer, ForeignKey('binary_question.id'), nullable=True)
    binary_campaign_id = Column(Integer, ForeignKey('binary_campaign.id'), nullable=True)




