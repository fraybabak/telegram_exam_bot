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
        context = self.contextService.read(context_id)
        if context is None:
            raise Exception("Context not found")
        return self.binaryQuestionRepository.create(question=question, rating=rating, answer=answer, context_id=context)
