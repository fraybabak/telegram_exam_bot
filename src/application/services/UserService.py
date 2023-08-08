from application.domain.User import User
from injector import inject

from adapter.out.persistence.userRepository import UserRepository

class UserService:
    @inject
    def __init__(self, userRepository: UserRepository):
        self.userRepository = userRepository


    def create(self, external_id: int, name: str, username: str, language_code: str, is_bot: bool, is_premium: bool, first_name: str, last_name: str, link: str) -> User:
        user = User(external_id=external_id, name=name, username=username, language_code=language_code, is_bot=is_bot, is_premium=is_premium, first_name=first_name, last_name=last_name, link=link)
        return self.userRepository.create(user)
        
    def find_by_external_id(self, external_id: int) -> User:
        return self.userRepository.find_by_external_id(external_id)