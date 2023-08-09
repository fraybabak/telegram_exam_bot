from adapter.out.persistence.repository import Repository
from application.domain.User import User
from adapter.out.persistence.models.user import UserModel
from database import session
class UserRepository(Repository):
    def __init__(self):
        self.db = session
        self.model = UserModel

    def create(self, user: User) -> User:
        if self.check_if_user_exists(user.external_id):
            return User(id=user.id, external_id=user.external_id, name=user.name, username=user.username, language_code=user.language_code, is_bot=user.is_bot, is_premium=user.is_premium, first_name=user.first_name, last_name=user.last_name, link=user.link)

        user_model = self.model(external_id=user.external_id, name=user.name, username=user.username, language_code=user.language_code, is_bot=user.is_bot, is_premium=user.is_premium, first_name=user.first_name, last_name=user.last_name, link=user.link)
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        # type: ignore
        return User(id=user_model.id, external_id=user_model.external_id, name=user_model.name, username=user_model.username, language_code=user_model.language_code, is_bot=user_model.is_bot, is_premium=user_model.is_premium, first_name=user_model.first_name, last_name=user_model.last_name, link=user_model.link)

    def read(self, external_id: int) -> User:
        user_model = self.db.query(self.model).filter(
            self.model.external_id == external_id).first()
        if user_model is None:
            raise Exception("User not found")
        return User(id=user_model.id, external_id=user_model.external_id, name=user_model.name, username=user_model.username, language_code=user_model.language_code, is_bot=user_model.is_bot, is_premium=user_model.is_premium, first_name=user_model.first_name, last_name=user_model.last_name, link=user_model.link)
        

    def find_by_external_id(self, external_id: int) -> User:
        user_model = self.db.query(self.model).filter(
            self.model.external_id == external_id).first()
        if user_model is None:
            return None
        return User(id=user_model.id, external_id=user_model.external_id, name=user_model.name, username=user_model.username, language_code=user_model.language_code, is_bot=user_model.is_bot, is_premium=user_model.is_premium, first_name=user_model.first_name, last_name=user_model.last_name, link=user_model.link)

    def check_if_user_exists(self, external_id: int) -> bool:
        user_model = self.db.query(self.model).filter(
            self.model.external_id == external_id).first()
        if user_model is None:
            return False
        return True


    def update(self, external_id: int, data:User) -> None:
        user_model = self.db.query(self.model).filter(external_id == external_id).first()
        if user_model is None:
            raise Exception("User not found")
        user_model.name = data.name
        user_model.username = data.username
        user_model.language_code = data.language_code
        user_model.is_bot = data.is_bot
        user_model.is_premium = data.is_premium
        user_model.first_name = data.first_name
        user_model.last_name = data.last_name
        user_model.link = data.link
        self.db.commit()
        self.db.refresh(user_model)

        

    def delete(self, external_id: int) -> None:
        user_model = self.db.query(self.model).filter(external_id == external_id).first()
        if user_model is None:
            raise Exception("User not found")
        self.db.delete(user_model)
        self.db.commit()

    def list_all(self):
        return self.db.query(self.model).all()