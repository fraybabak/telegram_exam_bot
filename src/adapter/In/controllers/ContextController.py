from application.services.ContextService import ContextService
from injector import inject
class ContextController:
    @inject
    def __init__(self, context_service: ContextService):
        self.context_service = context_service

    def create(self, description: str) -> None:
        self.context_service.create(description)