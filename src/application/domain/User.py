
class User:
    def __init__(self, name: str, username: str, language_code: str, is_bot: bool, is_premium: bool, first_name: str, last_name: str, link: str, external_id: int, id: int = None):
        self.id = id
        self.name = name
        self.username = username
        self.language_code = language_code
        self.is_bot = is_bot
        self.is_premium = is_premium
        self.first_name = first_name
        self.last_name = last_name
        self.link = link
        self.external_id = external_id

    def __str__(self):
        return f"User(id={self.id}, name={self.name}, username={self.username}, language_code={self.language_code}, is_bot={self.is_bot}, is_premium={self.is_premium})"

    def __repr__(self):
        return self.__str__()