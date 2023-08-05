class Context:
    def __init__(self, description: str, id: int = None):  # type: ignore
        """
        :param description: The description of the context.
        """
        self.description: str = description
        self.id: int = id

    def __str__(self):
        return self.description
