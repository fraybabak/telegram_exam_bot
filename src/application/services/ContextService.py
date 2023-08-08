
from application.domain.Context import Context
from adapter.out.persistence.contextRepository import ContextRepository
from injector import inject

class ContextService:
    @inject
    def __init__(self, contextRepository: ContextRepository):
        self.contextRepository = contextRepository

    def create(self, description: str, title:str) -> Context:
        return self.contextRepository.create(Context(description, title))

    def read(self, id: int) -> Context:
        return self.contextRepository.read(id)
    
    def find_by_description(self, description: str) -> Context:
        return self.contextRepository.find_by_description(description)

    def update(self, id: int, description: str) -> None:
        self.contextRepository.update(id, Context(description))

    def delete(self, id: int) -> None:
        self.contextRepository.delete(id)

    def list_all(self) -> None:
        for context in self.contextRepository.list_all():
            print(context)