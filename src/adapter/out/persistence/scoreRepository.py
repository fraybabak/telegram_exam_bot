from adapter.out.persistence.repository import Repository

from application.domain.Score import Score
from typing import List
from injector import inject
from database import session
from adapter.out.persistence.models.score import ScoreModel



class ScoreRepository(Repository):
    @inject
    def __init__(self):
        self.db = session
        self.model = ScoreModel

    def create(self, user_id:int, campaign_id:int, context_id:int, score:int, score_percent:float) -> Score:
        score_model = self.model(user_id=user_id, campaign_id=campaign_id, context_id=context_id, score=score, score_percent=score_percent)
        self.db.add(score_model)
        self.db.commit()
        self.db.refresh(score_model)
        return Score(id=score_model.id, user_id=score_model.user_id, campaign_id=score_model.campaign_id, context_id=score_model.context_id, score=score_model.score, score_percent=score_model.score_percent)