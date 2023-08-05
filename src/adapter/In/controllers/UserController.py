
from application.domain.User import User
from injector import inject
from application.services.UserService import UserService

class UserController:
    @inject
    def __init__(self, userService: UserService):
        self.userService = userService

    def create(self, external_id: int, name: str, username: str, language_code: str, is_bot: bool, is_premium: bool, first_name: str, last_name: str, link: str) -> User:
        return self.userService.create(external_id=external_id, name=name, username=username, language_code=language_code, is_bot=is_bot, is_premium=is_premium, first_name=first_name, last_name=last_name, link=link)

    # def read(self, id: int) -> User:
    #     return self.userService.read(id)

    # def find_by_external_id(self, external_id: int) -> User:
    #     return self.userService.find_by_external_id(external_id)

    # def update(self, id: int, external_id: int, name: str, username: str, language_code: str, is_bot: bool, is_premium: bool, first_name: str, last_name: str, link: str) -> None:
    #     self.userService.update(id, external_id, name, username, language_code, is_bot, is_premium, first_name, last_name, link)

    # def delete(self, id: int) -> None:
    #     self.userService.delete(id)

    # def list_all(self) -> None:
    #     for user in self.userService.list_all():
    #         print(user)