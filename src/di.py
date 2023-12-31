from injector import Injector




from application.services.ContextService import ContextService
from application.services.UserService import UserService
from application.services.AnswerService import answerService
from application.services.QuestionService import questionService
from application.services.CampaignService import campaignService
from application.services.ScoreService import ScoreService
from application.services.ReportService import ReportService

from adapter.In.controllers.ContextController import ContextController
from adapter.In.controllers.CampaingController import CampaignController
from adapter.In.controllers.AnswerController import AnswerController
from adapter.In.controllers.QuestionController import QuestionController
from adapter.In.controllers.ScoreController import ScoreController


from adapter.In.controllers.UserController import UserController

injector = Injector()

answerService = injector.get(answerService)
questionService = injector.get(questionService)
contextService = injector.get(ContextService)

scoreService = injector.get(ScoreService)
userService = injector.get(UserService)
campaignService = injector.get(campaignService)
contextController = injector.get(ContextController)
userController = injector.get(UserController)
answerController = injector.get(AnswerController)
campaignController = injector.get(CampaignController)
questionController = injector.get(QuestionController)
scoreController = injector.get(ScoreController)





