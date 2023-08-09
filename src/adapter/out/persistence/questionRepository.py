

from adapter.out.persistence.repository import Repository

from adapter.out.persistence.models.question import QuestionModel
from application.domain.Question import Question
from typing import List
from injector import inject
from database import session


class QuestionRepository(Repository):
    @inject
    def __init__(self):
        self.db = session
        self.model = QuestionModel

    def create(self, question, answer, rating, context_id) -> Question:
        question_model = self.model(
            question=question, rating=rating, answer=answer, context_id=context_id)
        self.db.add(question_model)
        self.db.commit()
        # self.db.refresh(question_model)
        return Question(id=question_model.id, question=question_model.question, context_id=question_model.context_id, answer=question_model.answer, rating=question_model.rating)  # type: ignore

    def read(self, id: int) -> Question:
        question_model = self.db.query(
            self.model).filter(self.model.id == id).first()
        if question_model is None:
            raise Exception("Question not found")
        return Question(id=question_model.id, question=question_model.question, context=question_model.context, answer=question_model.answer, rating=question_model.rating)

    def find_by_question(self, question: str) -> Question:
        question_model = self.db.query(self.model).filter(
            self.model.question == question).first()
        if question_model is None:
            raise Exception("Question not found")
        return Question(id=question_model.id, question=question_model.question, context=question_model.context, answer=question_model.answer, rating=question_model.rating)

    def find_by_context(self, context_id: int) -> List[Question]:
        question_model = self.db.query(self.model).filter(
            self.model.context_id == context_id).all()
        if question_model is None:
            raise Exception("Question not found")
        return [Question(id=question_model.id, question=question_model.question, context_id=question_model.context_id, answer=question_model.answer, rating=question_model.rating) for question_model in question_model]

    def update(self, id: int, question: Question) -> Question:

        question_model = self.db.query(
            self.model).filter(self.model.id == id).first()
        if question_model is None:
            raise Exception("Question not found")
        question_model.question = question.question
        question_model.context = question.context
        question_model.answer = question.answer
        question_model.rating = question.rating
        self.db.commit()
        self.db.refresh(question_model)
        return Question(id=question_model.id, question=question_model.question, context=question_model.context, answer=question_model.answer, rating=question_model.rating)

    def delete(self, id: int) -> bool:
        question_model = self.db.query(
            self.model).filter(self.model.id == id).first()
        if question_model is None:
            raise Exception("Question not found")
        self.db.delete(question_model)
        self.db.commit()
        return True
