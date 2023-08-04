

from abc import ABC

class Repository(ABC):
    def __init__(self, db ):
        self.db = db

    def create(self, data):
        pass

    def read(self, id):

        pass

    def update(self, id: int, data) -> None:
        pass

    def delete(self, id: int) -> None:
        pass

    def list_all(self):
        pass