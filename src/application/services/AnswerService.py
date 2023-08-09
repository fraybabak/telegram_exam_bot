from application.domain.Answer import Answer
from injector import inject

from adapter.out.persistence.answerRepository import AnswerRepository


class answerService:
    @inject
    def __init__(self, answerRepository: AnswerRepository):
        self.answerRepository = answerRepository

    def create(self, answer: bool, question_id: int, user_id: int, campaign_id:int) -> Answer:
        return self.answerRepository.create(answer=answer, question_id=question_id, user_id=user_id, campaign_id=campaign_id)