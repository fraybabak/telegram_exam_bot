from application.domain.Campaign  import Campaign
from injector import inject
from datetime import datetime

from adapter.out.persistence.campaignRepository import CampaignRepository

class campaignService:
    @inject
    def __init__(self, campaignRepository: CampaignRepository):
        self.campaignRepository = campaignRepository

    def create(self, user_id:int, context_id:int) -> Campaign:
        created_at = datetime.now()
        updated_at = datetime.now()
        campaign = Campaign(user_id=user_id, context_id=context_id, created_at=created_at, updated_at=updated_at, is_active=True)
        return self.campaignRepository.create(campaign)