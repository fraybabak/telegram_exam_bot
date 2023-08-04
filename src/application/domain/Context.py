class Context:
    def __init__(self, description: str, id: int = None):
        """
        :param description: The description of the context.
        """
        self.description = description
        self.id = id

    def __str__(self):
        return self.description