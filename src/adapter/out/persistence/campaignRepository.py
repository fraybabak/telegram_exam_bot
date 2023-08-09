from adapter.out.persistence.repository import Repository

from application.domain.Campaign import Campaign
from typing import List
from injector import inject
from database import session
from adapter.out.persistence.models.campaign import CampaignModel



class CampaignRepository(Repository):
    @inject
    def __init__(self):
        self.db = session
        self.model = CampaignModel
    
    def create(self, campaign: Campaign) -> Campaign:
        campaign_model = self.model(user_id=campaign.user_id, context_id=campaign.context_id, created_at=campaign.created_at, updated_at=campaign.updated_at, is_active=campaign.is_active)
        self.db.add(campaign_model)
        self.db.commit()
        self.db.refresh(campaign_model)
        return Campaign(id=campaign_model.id, user_id=campaign_model.user_id, context_id=campaign_model.context_id, created_at=campaign_model.created_at, updated_at=campaign_model.updated_at, is_active=campaign_model.is_active)
    
    def read(self, id: int) -> Campaign:
        campaign_model = self.db.query(self.model).filter(self.model.id == id).first()
        if campaign_model is None:
            raise Exception("Campaign not found")

        return Campaign(id=campaign_model.id, user_id=campaign_model.user_id, context_id=campaign_model.context_id, created_at=campaign_model.created_at, updated_at=campaign_model.updated_at, is_active=campaign_model.is_active)


    def find_by_user(self, user_id: int) -> List[Campaign]:
        campaign_model = self.db.query(self.model).filter(self.model.user_id == user_id).all()
        if campaign_model is None:
            raise Exception("Campaign not found")
        return [Campaign(id=campaign_model.id, user_id=campaign_model.user_id, context_id=campaign_model.context_id, created_at=campaign_model.created_at, updated_at=campaign_model.updated_at, is_active=campaign_model.is_active) for campaign_model in campaign_model]

    def find_by_context(self, context_id: int) -> List[Campaign]:
        campaign_model = self.db.query(self.model).filter(self.model.context_id == context_id).all()
        if campaign_model is None:
            raise Exception("Campaign not found")
        return [Campaign(id=campaign_model.id, user_id=campaign_model.user_id, context_id=campaign_model.context_id, created_at=campaign_model.created_at, updated_at=campaign_model.updated_at, is_active=campaign_model.is_active) for campaign_model in campaign_model]

    def find_by_user_and_context(self, user_id: int, context_id: int) -> Campaign:
        campaign_model = self.db.query(self.model).filter(self.model.user_id == user_id, self.model.context_id == context_id).first()
        if campaign_model is None:
            raise Exception("Campaign not found")
        return Campaign(id=campaign_model.id, user_id=campaign_model.user_id, context_id=campaign_model.context_id, created_at=campaign_model.created_at, updated_at=campaign_model.updated_at, is_active=campaign_model.is_active)