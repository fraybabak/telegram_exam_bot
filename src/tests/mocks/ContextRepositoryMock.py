from adapter.out.persistence.repository import Repository


class ContextRepositoryMock(Repository):
    def __init__(self):
        self.contexts = []

    def create(self, context):
        context.id = len(self.contexts) + 1
        self.contexts.append(context)
        return context

    def read(self, id):
        for context in self.contexts:
            if context.id == id:
                return context
        raise Exception("Context not found")

    def update(self, context):
        for i in range(len(self.contexts)):
            if self.contexts[i].id == context.id:
                self.contexts[i] = context
                return context
        raise Exception("Context not found")

    def delete(self, id):
        for i in range(len(self.contexts)):
            if self.contexts[i].id == id:
                del self.contexts[i]
                return True
        raise Exception("Context not found")

    def findByDescription(self, description):
        for context in self.contexts:
            if context.description == description:
                return context
        raise Exception("Context not found")

    def list(self):
        return self.contexts
