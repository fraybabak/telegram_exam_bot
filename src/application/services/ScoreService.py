from application.domain.Score import Score
from injector import inject

from adapter.out.persistence.scoreRepository import ScoreRepository
from adapter.out.persistence.campaignRepository import CampaignRepository
from adapter.out.persistence.answerRepository import AnswerRepository
from adapter.out.persistence.questionRepository import QuestionRepository
from adapter.out.persistence.userRepository import UserRepository
from adapter.out.persistence.contextRepository import ContextRepository



def monitize_option(option):
    if option == 1:
        return 'کاملا مخالفم'
    elif option == 2:
        return 'مخالفم'
    elif option == 3:
        return 'متوسط'
    elif option == 4:
        return 'موافقم'
    elif option == 5:
        return 'کاملا موافقم'
    else:
        return 'نمیدانم'
class ScoreService:
    @inject
    def __init__(self, scoreRepository: ScoreRepository, campaignRepository: CampaignRepository, answerRepository: AnswerRepository, questionRepository: QuestionRepository, userRepository: UserRepository, contextRepository: ContextRepository):
        self.scoreRepository = scoreRepository
        self.campaignRepository = campaignRepository
        self.answerRepository = answerRepository
        self.questionRepository = questionRepository
        self.userRepository = userRepository
        self.contextRepository = contextRepository

    def create(self, campaign_id: int, user_id:int):
        campaign = self.campaignRepository.read(campaign_id)
        if campaign is None:
            raise Exception("Campaign not found")
        user = self.userRepository.read(user_id)
        if user is None:
            raise Exception("User not found")
        context = self.contextRepository.read(campaign.context_id)
        if context is None:
            raise Exception("Context not found")
        answers = self.answerRepository.find_by_campaign(campaign_id)
        if answers is None:
            raise Exception("Answer not found")
        questions = self.questionRepository.find_by_context(campaign.context_id)
        if questions is None:
            raise Exception("Questions not found")
        object_answers = [
            { "question_id": answer.question_id, "answer": answer.answer, 'rating': questions[answer.question_id].rating, "question": questions[answer.question_id].question, 'answer_id': answer.id, 'answer_str': monitize_option(answer.answer) } for answer in answers
        ]
        score = sum([answer['answer'] * answer['rating'] for answer in object_answers])
        max_score = sum([5 * answer['rating'] for answer in object_answers])
        score_percent = (score / max_score) * 100
        score_domain =  self.scoreRepository.create(score=score, score_percent=score_percent, user_id=user_id, campaign_id=campaign_id, context_id=campaign.context_id)

        return {
            "score": int(score_domain.score),
            "max_score": max_score,
            "score_percent": int(score_domain.score_percent),
            "user": {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
            "campaign_id": score_domain.campaign_id,
            "questions_and_answers": object_answers,
            "quiz": {
                "id": context.id,
                "quiz_title": context.title,
                "quiz_description": context.description,
            }
        }
