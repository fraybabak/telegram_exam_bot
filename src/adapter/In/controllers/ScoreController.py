from application.services.ScoreService import ScoreService
from application.services.ReportService import ReportService
from application.domain.Score import Score
from injector import inject
from typing import List

class ScoreController:
    @inject
    def __init__(self, score_service: ScoreService, report_service: ReportService):
        self.score_service = score_service
        self.report_service = report_service

    def create(self, campaign_id: int, user_id:int):
        report = self.score_service.create(campaign_id, user_id)
        return self.report_service.create_report(report)
