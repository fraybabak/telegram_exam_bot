from sqlalchemy import Column, Integer, Boolean, ForeignKey, Text
from database import Base, session





class BinaryAnswerModel(Base):
    __tablename__ = 'binary_answers'
    id = Column(Integer, primary_key=True)
    answer = Column(Boolean)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    campaign_id = Column(Integer, ForeignKey('campaign.id'), nullable=True)
    binary_questions_id = Column(Integer, ForeignKey('binary_questions.id'), nullable=True)



Base.metadata.create_all(session.bind)
