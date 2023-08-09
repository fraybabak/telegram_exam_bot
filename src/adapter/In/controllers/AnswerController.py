from application.domain.Answer import Answer
from injector import inject
from application.services.AnswerService import answerService


class AnswerController:
    @inject
    def __init__(self, answerService: answerService):
        self.answerService = answerService

    def create(self, answer: int, question_id: int, user_id: int, campaign_id:int) -> Answer:
        return self.answerService.create(answer=answer,question_id= question_id, user_id=user_id, campaign_id=campaign_id)