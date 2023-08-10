from sqlalchemy import Column,Date, Integer, Boolean, ForeignKey, Text, Float
from database import Base, session



class ScoreModel(Base):
    __tablename__ = 'score'
    id = Column(Integer, primary_key=True)
    context_id = Column(Integer, ForeignKey('context.id'), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    score = Column(Integer)
    score_percent = Column(Float)
    campaign_id = Column(Integer, ForeignKey('campaign.id'), nullable=True)


Base.metadata.create_all(session.bind)