


from adapter.out.persistence.repository import Repository

from adapter.out.persistence.models.binaryQuestion import BinaryQuestionModel
from application.domain.BinaryQuestion import BinaryQuestion
from typing import List
from injector import inject
from database import session

class binaryQuestionRepository(Repository):
    @inject
    def __init__(self):
        self.db = session
        self.model = BinaryQuestionModel
    
    def create(self, binaryQuestion: BinaryQuestion) -> BinaryQuestion:
        binaryQuestion_model = self.model(question=binaryQuestion.question, context_id=binaryQuestion.context.id, answer=binaryQuestion.answer, rating=binaryQuestion.rating, answer=binaryQuestion.answer)
        self.db.add(binaryQuestion_model)
        self.db.commit()
        self.db.refresh(binaryQuestion_model)
        return BinaryQuestion(id=binaryQuestion_model.id, question=binaryQuestion_model.question, context=binaryQuestion_model.context, answer=binaryQuestion_model.answer, rating=binaryQuestion_model.rating)

    def read(self, id: int) -> BinaryQuestion:
        binaryQuestion_model = self.db.query(self.model).filter(self.model.id == id).first()
        if binaryQuestion_model is None:
            raise Exception("BinaryQuestion not found")
        return BinaryQuestion(id=binaryQuestion_model.id, question=binaryQuestion_model.question, context=binaryQuestion_model.context, answer=binaryQuestion_model.answer, rating=binaryQuestion_model.rating)
    
    def find_by_question(self, question: str) -> BinaryQuestion:
        binaryQuestion_model = self.db.query(self.model).filter(self.model.question == question).first()
        if binaryQuestion_model is None:
            raise Exception("BinaryQuestion not found")
        return BinaryQuestion(id=binaryQuestion_model.id, question=binaryQuestion_model.question, context=binaryQuestion_model.context, answer=binaryQuestion_model.answer, rating=binaryQuestion_model.rating)
    
    def find_by_context(self, context_id: int) -> List[BinaryQuestion]:
        binaryQuestion_model = self.db.query(self.model).filter(self.model.context_id == context_id).all()
        if binaryQuestion_model is None:
            raise Exception("BinaryQuestion not found")
        return [BinaryQuestion(id=binaryQuestion_model.id, question=binaryQuestion_model.question, context=binaryQuestion_model.context, answer=binaryQuestion_model.answer, rating=binaryQuestion_model.rating) for binaryQuestion_model in binaryQuestion_model]
    
    def update(self, id: int, binaryQuestion: BinaryQuestion) -> BinaryQuestion:
            
        binaryQuestion_model = self.db.query(self.model).filter(self.model.id == id).first()
        if binaryQuestion_model is None:
            raise Exception("BinaryQuestion not found")
        binaryQuestion_model.question = binaryQuestion.question
        binaryQuestion_model.context = binaryQuestion.context
        binaryQuestion_model.answer = binaryQuestion.answer
        binaryQuestion_model.rating = binaryQuestion.rating
        self.db.commit()
        self.db.refresh(binaryQuestion_model)
        return BinaryQuestion(id=binaryQuestion_model.id, question=binaryQuestion_model.question, context=binaryQuestion_model.context, answer=binaryQuestion_model.answer, rating=binaryQuestion_model.rating)
    
    def delete(self, id: int) -> bool:
        binaryQuestion_model = self.db.query(self.model).filter(self.model.id == id).first()
        if binaryQuestion_model is None:
            raise Exception("BinaryQuestion not found")
        self.db.delete(binaryQuestion_model)
        self.db.commit()
        return True
    