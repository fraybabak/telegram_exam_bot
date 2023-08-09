from typing import List
from application.domain.Context import Context
from application.domain.Question import Question
from adapter.out.persistence.questionRepository import QuestionRepository
from injector import inject

from application.services.ContextService import ContextService


class questionService:
    @inject
    def __init__(self, questionRepository: QuestionRepository, contextService: ContextService):
        self.questionRepository = questionRepository
        self.contextService = contextService

    def create(self, question, answer, rating, context_id: int) -> Question:
        return self.questionRepository.create(question=question, rating=rating, answer=answer, context_id=context_id)
    
    def find_by_id(self, id: int) -> Question:
        return self.questionRepository.read(id=id)
    
    def find_by_question(self, question: str) -> Question:
        return self.questionRepository.find_by_question(question=question)
    
    def find_by_context(self, context_id: int) -> List[Question]:
        return self.questionRepository.find_by_context(context_id=context_id)
    def find_by_context_and_rating(self, context_id: int, rating: int) -> List[Question]:
        return self.questionRepository.find_by_context_and_rating(context_id=context_id, rating=rating)
    
