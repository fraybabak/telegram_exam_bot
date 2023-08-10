class Score(object):
    def __init__(self, score:int, campaign_id:int, user_id:float, score_percent:int,context_id:int, id=None):
        self.id = id
        self.user_id = user_id
        self.campaign_id = campaign_id
        self.context_id = context_id
        self.score = score
        self.score_percent = score_percent

    def __str__(self):
        return f"Score: {self.score} - Score Percentage: {self.score_percent} - Campain Id: {self.campaign_id} - User Id: {self.user_id} - Id: {self.id}"