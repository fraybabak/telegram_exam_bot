from sqlalchemy import Column, Integer, Boolean, ForeignKey, Text
from database import Base, session





class AnswerModel(Base):
    __tablename__ = 'answer'
    id = Column(Integer, primary_key=True)
    answer = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    question_id = Column(Integer, ForeignKey('question.id'), nullable=True)
    campaign_id = Column(Integer, ForeignKey('campaign.id'), nullable=True)




