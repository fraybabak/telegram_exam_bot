from application.domain.BinaryQuestion import BinaryQuestion
from injector import inject
from application.services.binaryQuestionService import BinaryQuestionService


class BinaryQuestionController:
    @inject
    def __init__(self, binaryQuestionService: BinaryQuestionService):
        self.binaryQuestionService = binaryQuestionService

    def find_by_id(self, id: int) -> BinaryQuestion:
        return self.binaryQuestionService.find_by_id(id)
    def find_by_context_id(self, context_id: int) -> list[BinaryQuestion]:
        return self.binaryQuestionService.find_by_context(context_id)