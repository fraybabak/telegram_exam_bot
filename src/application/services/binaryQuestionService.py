from typing import List
from application.domain.Context import Context
from application.domain.BinaryQuestion import BinaryQuestion
from adapter.out.persistence.binaryQuestionRepository import BinaryQuestionRepository
from injector import inject

from application.services.ContextService import ContextService


class BinaryQuestionService:
    @inject
    def __init__(self, binaryQuestionRepository: BinaryQuestionRepository, contextService: ContextService):
        self.binaryQuestionRepository = binaryQuestionRepository
        self.contextService = contextService

    def create(self, question, answer, rating, context_id: int) -> BinaryQuestion:
        return self.binaryQuestionRepository.create(question=question, rating=rating, answer=answer, context_id=context_id)
    
    def find_by_id(self, id: int) -> BinaryQuestion:
        return self.binaryQuestionRepository.read(id=id)
    
    def find_by_question(self, question: str) -> BinaryQuestion:
        return self.binaryQuestionRepository.find_by_question(question=question)
    
    def find_by_context(self, context_id: int) -> List[BinaryQuestion]:
        return self.binaryQuestionRepository.find_by_context(context_id=context_id)
    def find_by_context_and_rating(self, context_id: int, rating: int) -> List[BinaryQuestion]:
        return self.binaryQuestionRepository.find_by_context_and_rating(context_id=context_id, rating=rating)
    
