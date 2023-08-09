from sqlalchemy import Column,Date, Integer, Boolean, ForeignKey, Text
from database import Base, session




class CampaignModel(Base):
    __tablename__ = 'campaign'
    id = Column(Integer, primary_key=True)
    context_id = Column(Integer, ForeignKey('context.id'), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    is_active = Column(Boolean)
    end_date = Column(Date)
    created_at = Column(Date)
    updated_at = Column(Date)

Base.metadata.create_all(session.bind)