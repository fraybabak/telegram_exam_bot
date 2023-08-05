from application.domain.BinaryAnswer import BinaryAnswer
from injector import inject

from adapter.out.persistence.binaryAnswerRepository import BinaryAnswerRepository


class BinaryAnswerService:
    @inject
    def __init__(self, binaryAnswerRepository: BinaryAnswerRepository):
        self.binaryAnswerRepository = binaryAnswerRepository

    def create(self, answer: bool, question_id: int, user_id: int, campaign_id:int) -> BinaryAnswer:
        binaryAnswer = BinaryAnswer(answer=answer, question_id=question_id, user_id=user_id, campaign_id=campaign_id)
        return self.binaryAnswerRepository.create(binaryAnswer)