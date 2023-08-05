from application.services.ContextService import ContextService
from application.domain.Context import Context
from injector import inject
class ContextController:
    @inject
    def __init__(self, context_service: ContextService):
        self.context_service = context_service

    def create(self, description: str) -> Context:
        return self.context_service.create(description)