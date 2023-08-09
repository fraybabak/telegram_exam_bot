from typing import List
from injector import inject
from database import session
from adapter.out.persistence.repository import Repository
from application.domain.Answer import Answer
from adapter.out.persistence.models.answer import AnswerModel


class AnswerRepository(Repository):
    @inject
    def __init__(self):
        self.db = session
        self.model = AnswerModel

    def create(self, answer, question_id, user_id, campaign_id) -> Answer:
        answer_model = self.exists_by_question_campaign_and_user(
            question_id=question_id, campaign_id=campaign_id, user_id=user_id)
        if answer_model:
            raise Exception("Answer already exists")
        answer_model = self.model(
            answer=answer, question_id=question_id, user_id=user_id, campaign_id=campaign_id)
        self.db.add(answer_model)
        self.db.commit()
        self.db.refresh(answer_model)
        return Answer(id=answer_model.id, answer=answer_model.answer, question_id=answer_model.question_id, user_id=answer_model.user_id, campaign_id=answer_model.campaign_id) 
    
    def read(self, id: int) -> Answer:
        answer_model = self.db.query(
            self.model).filter(self.model.id == id).first()
        if answer_model is None:
            raise Exception("Answer not found")
        return Answer(id=answer_model.id, answer=answer_model.answer, question_id=answer_model.question_id, user_id=answer_model.user_id, campaign_id=answer_model.campaign_id)

    def find_by_question(self, question_id: int) -> Answer:
        answer_model = self.db.query(self.model).filter(
            self.model.question_id == question_id).first()
        if answer_model is None:
            raise Exception("Answer not found")
        return Answer(id=answer_model.id, answer=answer_model.answer, question_id=answer_model.question_id, user_id=answer_model.user_id, campaign_id=answer_model.campaign_id)

    def find_by_user(self, user_id: int) -> List[Answer]:
        answer_model = self.db.query(self.model).filter(
            self.model.user_id == user_id).all()
        if answer_model is None:
            raise Exception("Answer not found")
        return [Answer(id=answer_model.id, answer=answer_model.answer, question_id=answer_model.question_id, user_id=answer_model.user_id, campaign_id=answer_model.campaign_id) for answer_model in answer_model]

    def find_by_campaign(self, campaign_id: int) -> List[Answer]:
        answer_model = self.db.query(self.model).filter(
            self.model.campaign_id == campaign_id).all()
        if answer_model is None:
            raise Exception("Answer not found")
        return [Answer(id=answer_model.id, answer=answer_model.answer, question_id=answer_model.question_id, user_id=answer_model.user_id, campaign_id=answer_model.campaign_id) for answer_model in answer_model]

    def find_by_question_and_user(self, question_id: int, user_id: int) -> Answer:
        answer_model = self.db.query(self.model).filter(
            self.model.question_id == question_id, self.model.user_id == user_id).first()
        if answer_model is None:
            raise Exception("Answer not found")
        return Answer(id=answer_model.id, answer=answer_model.answer, question_id=answer_model.question_id, user_id=answer_model.user_id, campaign_id=answer_model.campaign_id)
    def exists_by_question_campaign_and_user(self, question_id: int, campaign_id: int, user_id: int) -> bool:
        answer_model = self.db.query(self.model).filter(
            self.model.question_id == question_id, self.model.campaign_id == campaign_id, self.model.user_id == user_id).first()
        if  answer_model is None:
            return False
        return True

    def find_by_question_and_campaign_and_user(self, question_id: int, campaign_id: int, user_id:id) -> List[Answer]:
        answer_model = self.db.query(self.model).filter(
            self.model.question_id == question_id, self.model.question_id == campaign_id, self.model.user_id == user_id).all()
        if answer_model is None:
            raise Exception("Answer not found")
        return [Answer(id=answer_model.id, answer=answer_model.answer, question_id=answer_model.question_id, user_id=answer_model.user_id, campaign_id=answer_model.campaign_id) for answer_model in answer_model]
