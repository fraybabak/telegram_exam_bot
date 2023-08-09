from application.services.ContextService import ContextService
from application.domain.Context import Context
from injector import inject
from typing import List
class ContextController:
    @inject
    def __init__(self, context_service: ContextService):
        self.context_service = context_service

    def create(self, description: str, title:str) -> Context:
        return self.context_service.create(description, title)
    def find_by_id(self, id: int) -> Context:
        return self.context_service.find_by_id(id)
    def find_by_description(self, description: str) -> Context:
        return self.context_service.find_by_description(description)
    def list_all(self)-> List[Context]:
        return self.context_service.list_all()
