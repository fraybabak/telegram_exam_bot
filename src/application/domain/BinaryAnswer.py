class BinaryAnswer:
    def __init__(self, answer: bool, question_id: int, user_id: int, campaign_id:int, id: int = None):
        self.answer = answer
        self.question_id = question_id
        self.user_id = user_id
        self.campaign_id = campaign_id
        self.id = id

    def __str__(self):
        return str(self.answer)

    def __repr__(self):
        return str(self)