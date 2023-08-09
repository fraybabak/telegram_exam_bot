from application.domain.Question import Question
from injector import inject
from application.services.QuestionService import questionService


class QuestionController:
    @inject
    def __init__(self, questionService: questionService):
        self.questionService = questionService

    def find_by_id(self, id: int) -> Question:
        return self.questionService.find_by_id(id)
    def find_by_context_id(self, context_id: int) -> list[Question]:
        return self.questionService.find_by_context(context_id)