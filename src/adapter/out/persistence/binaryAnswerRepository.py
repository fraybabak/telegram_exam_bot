from typing import List
from injector import inject
from database import session
from adapter.out.persistence.repository import Repository
from application.domain.BinaryAnswer import BinaryAnswer
from adapter.out.persistence.models.binaryAnswer import BinaryAnswerModel


class BinaryAnswerRepository(Repository):
    @inject
    def __init__(self):
        self.db = session
        self.model = BinaryAnswerModel

    def create(self, answer, question_id, user_id, campaign_id) -> BinaryAnswer:
        binaryAnswer_model = self.find_by_question_and_campaign_and_user(
            question_id, campaign_id, user_id)
        if binaryAnswer_model is not None:
            raise Exception("BinaryAnswer already exists")
        binaryAnswer_model = self.model(
            answer=answer, question_id=question_id, user_id=user_id, campaign_id=campaign_id)
        self.db.add(binaryAnswer_model)
        self.db.commit()
        self.db.refresh(binaryAnswer_model)
        return BinaryAnswer(id=binaryAnswer_model.id, answer=binaryAnswer_model.answer, question_id=binaryAnswer_model.question_id, user_id=binaryAnswer_model.user_id, campaign_id=binaryAnswer_model.campaign_id) 
    
    def read(self, id: int) -> BinaryAnswer:
        binaryAnswer_model = self.db.query(
            self.model).filter(self.model.id == id).first()
        if binaryAnswer_model is None:
            raise Exception("BinaryAnswer not found")
        return BinaryAnswer(id=binaryAnswer_model.id, answer=binaryAnswer_model.answer, question_id=binaryAnswer_model.question_id, user_id=binaryAnswer_model.user_id, campaign_id=binaryAnswer_model.campaign_id)

    def find_by_question(self, question_id: int) -> BinaryAnswer:
        binaryAnswer_model = self.db.query(self.model).filter(
            self.model.question_id == question_id).first()
        if binaryAnswer_model is None:
            raise Exception("BinaryAnswer not found")
        return BinaryAnswer(id=binaryAnswer_model.id, answer=binaryAnswer_model.answer, question_id=binaryAnswer_model.question_id, user_id=binaryAnswer_model.user_id, campaign_id=binaryAnswer_model.campaign_id)

    def find_by_user(self, user_id: int) -> List[BinaryAnswer]:
        binaryAnswer_model = self.db.query(self.model).filter(
            self.model.user_id == user_id).all()
        if binaryAnswer_model is None:
            raise Exception("BinaryAnswer not found")
        return [BinaryAnswer(id=binaryAnswer_model.id, answer=binaryAnswer_model.answer, question_id=binaryAnswer_model.question_id, user_id=binaryAnswer_model.user_id, campaign_id=binaryAnswer_model.campaign_id) for binaryAnswer_model in binaryAnswer_model]

    def find_by_campaign(self, campaign_id: int) -> List[BinaryAnswer]:
        binaryAnswer_model = self.db.query(self.model).filter(
            self.model.campaign_id == campaign_id).all()
        if binaryAnswer_model is None:
            raise Exception("BinaryAnswer not found")
        return [BinaryAnswer(id=binaryAnswer_model.id, answer=binaryAnswer_model.answer, question_id=binaryAnswer_model.question_id, user_id=binaryAnswer_model.user_id, campaign_id=binaryAnswer_model.campaign_id) for binaryAnswer_model in binaryAnswer_model]

    def find_by_question_and_user(self, question_id: int, user_id: int) -> BinaryAnswer:
        binaryAnswer_model = self.db.query(self.model).filter(
            self.model.question_id == question_id, self.model.user_id == user_id).first()
        if binaryAnswer_model is None:
            raise Exception("BinaryAnswer not found")
        return BinaryAnswer(id=binaryAnswer_model.id, answer=binaryAnswer_model.answer, question_id=binaryAnswer_model.question_id, user_id=binaryAnswer_model.user_id, campaign_id=binaryAnswer_model.campaign_id)

    def find_by_question_and_campaign_and_user(self, question_id: int, campaign_id: int, user_id:id) -> List[BinaryAnswer]:
        binaryAnswer_model = self.db.query(self.model).filter(
            self.model.question_id == question_id, self.model.campaign_id == campaign_id, self.model.user_id == user_id).all()
        if binaryAnswer_model is None:
            raise Exception("BinaryAnswer not found")
        return [BinaryAnswer(id=binaryAnswer_model.id, answer=binaryAnswer_model.answer, question_id=binaryAnswer_model.question_id, user_id=binaryAnswer_model.user_id, campaign_id=binaryAnswer_model.campaign_id) for binaryAnswer_model in binaryAnswer_model]
