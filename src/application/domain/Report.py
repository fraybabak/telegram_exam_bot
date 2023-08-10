from typing import List, Dict

class Report:
    def __init__(self, score: float, max_score: float, score_percent: float, user: Dict[str, str], campaign_id: int, quiz: Dict[str, str], questions_and_answers: List[Dict[str, str]]):
        self.score = score
        self.max_score = max_score
        self.score_percent = score_percent
        self.user = user
        self.campaign_id = campaign_id
        self.quiz = quiz
        self.questions_and_answers = questions_and_answers