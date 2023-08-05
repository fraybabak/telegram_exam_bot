from application.domain.BinaryCampaign  import BinaryCampaign
from injector import inject
from datetime import datetime

from adapter.out.persistence.binaryCampaignRepository import BinaryCampaignRepository

class BinaryCampaignService:
    @inject
    def __init__(self, binaryCampaignRepository: BinaryCampaignRepository):
        self.binaryCampaignRepository = binaryCampaignRepository

    def create(self, user_id:int, context_id:int) -> BinaryCampaign:
        created_at = datetime.now()
        updated_at = datetime.now()
        binaryCampaign = BinaryCampaign(user_id=user_id, context_id=context_id, created_at=created_at, updated_at=updated_at, is_active=True)
        return self.binaryCampaignRepository.create(binaryCampaign)