from injector import Injector




from application.services.ContextService import ContextService
from application.services.UserService import UserService
from application.services.binaryAnswerService import BinaryAnswerService
from application.services.binaryQuestionService import BinaryQuestionService
from application.services.binaryCampaignService import BinaryCampaignService

from adapter.out.persistence.contextRepository import ContextRepository
from adapter.In.controllers.ContextController import ContextController
from adapter.In.controllers.BinaryCampaingController import BinaryCampaignController
from adapter.In.controllers.BinaryAnswerController import BinaryAnswerController

from adapter.In.controllers.UserController import UserController

injector = Injector()

contextRepository = injector.get(ContextRepository)
binaryAnswerService = injector.get(BinaryAnswerService)
binaryQuestionService = injector.get(BinaryQuestionService)
contextService = injector.get(ContextService)
userService = injector.get(UserService)
binaryCampaignService = injector.get(BinaryCampaignService)
contextController = injector.get(ContextController)
userController = injector.get(UserController)
binaryAnswerController = injector.get(BinaryAnswerController)
binaryCampaignController = injector.get(BinaryCampaignController)






