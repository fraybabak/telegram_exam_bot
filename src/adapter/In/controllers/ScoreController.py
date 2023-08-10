from application.services.ScoreService import ScoreService
from application.domain.Score import Score
from injector import inject
from typing import List

class ScoreController:
    @inject
    def __init__(self, score_service: ScoreService):
        self.score_service = score_service

    def create(self, campaign_id: int, user_id:int):
        return self.score_service.create(campaign_id, user_id)