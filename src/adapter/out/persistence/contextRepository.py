from application.domain.Context import Context
from adapter.out.persistence.repository import Repository
from adapter.out.persistence.models.context import ContextModel
from typing import List
from injector import inject
from database import session


class ContextRepository(Repository):
    @inject
    def __init__(self):
        self.db = session
        self.model = ContextModel

    def create(self, context: Context) -> Context:
        context_model = self.model(description=context.description)
        self.db.add(context_model)
        self.db.commit()
        self.db.refresh(context_model)
        return Context(id=context_model.id, description=context_model.description)

    def read(self, id: int) -> Context:
        context_model = self.db.query(self.model).filter(self.model.id == id).first()
        if context_model is None:
            raise Exception("Context not found")
        return Context(id=context_model.id, description=context_model.description)
    
    def find_by_description(self, description: str) -> Context:
        context_model = self.db.query(self.model).filter(self.model.description == description).first()
        if context_model is None:
            raise Exception("Context not found")
        return Context(id=context_model.id, description=context_model.description)

    def update(self, id: int, context: Context) -> Context:

        context_model = self.db.query(self.model).filter(self.model.id == id).first()
        if context_model is None:
            raise Exception("Context not found")
        context_model.description = context.description
        self.db.commit()
        self.db.refresh(context_model)
        return Context(id=context_model.id, description=context_model.description)
        

    def delete(self, id: int) -> bool:
        context_model = self.db.query(self.model).filter(self.model.id == id).first()
        if context_model is None:
            raise Exception("Context not found")
        self.db.delete(context_model)
        self.db.commit()
        return True

    def list_all(self) -> List[Context]:
        return [Context(id=context_model.id, description=context_model.description) for context_model in self.db.query(self.model).all()]