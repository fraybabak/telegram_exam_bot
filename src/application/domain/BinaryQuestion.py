from application.domain.Context import Context

class BinaryQuestion:
    def __init__(self, question: str, rating: int, context_id: int, id: int = None, answer: bool = None, ):
        """
        :param question: The question of the question.
        :param rating: The rating or weight associated with the question.
        """
        self.question = question
        self.rating = rating
        self.answer = answer
        self.context_id = context_id
        self.id = id


    def __str__(self):
        return f'Question: {self.text}\nRating: {self.rating}'