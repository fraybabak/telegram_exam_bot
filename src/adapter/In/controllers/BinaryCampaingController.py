from application.domain.BinaryCampaign  import BinaryCampaign
from injector import inject
from application.services.binaryCampaignService import BinaryCampaignService


class BinaryCampaignController:
    @inject
    def __init__(self, binaryCampaignService: BinaryCampaignService):
        self.binaryCampaignService = binaryCampaignService

    def create(self, user_id:int, context_id:int) -> BinaryCampaign:
        return self.binaryCampaignService.create(user_id, context_id)