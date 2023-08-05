import sys
import os

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from injector import Injector
from application.services.ContextService import ContextService
from tests.mocks.ContextRepositoryMock import ContextRepositoryMock


class ContextServiceTest:
    def __init__(self):
        self.injector = Injector()
        self.injector.binder.bind(
            ContextRepositoryMock, to=ContextRepositoryMock())
        self.contextService = self.injector.get(ContextService)

    def test_create(self):
        context = self.contextService.create("test")
        assert context.id > 0
        assert context.description == "test"

    def test_read(self):
        context = self.contextService.create("test")
        context2 = self.contextService.read(context.id)
        assert context2.id == context.id
        assert context2.description == context.description

    def test_update(self):
        context = self.contextService.create("test")
        context2 = self.contextService.update(context.id, "test2")
        assert context2.id == context.id  # type: ignore
        assert context2.description == "test2"  # type: ignore

    def test_delete(self):
        context = self.contextService.create("test")
        self.contextService.delete(context.id)
        assert self.contextService.read(context.id) is None
