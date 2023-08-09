from application.domain.Campaign  import Campaign
from injector import inject
from application.services.CampaignService import campaignService


class CampaignController:
    @inject
    def __init__(self, campaignService: campaignService):
        self.campaignService = campaignService

    def create(self, user_id:int, context_id:int) -> Campaign:
        return self.campaignService.create(user_id, context_id)