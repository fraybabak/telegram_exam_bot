from application.domain.BinaryAnswer import BinaryAnswer
from injector import inject
from application.services.binaryAnswerService import BinaryAnswerService


class BinaryAnswerController:
    @inject
    def __init__(self, binaryAnswerService: BinaryAnswerService):
        self.binaryAnswerService = binaryAnswerService

    def create(self, answer: bool, question_id: int, user_id: int, campaign_id:int) -> BinaryAnswer:
        return self.binaryAnswerService.create(answer, question_id, user_id, campaign_id)