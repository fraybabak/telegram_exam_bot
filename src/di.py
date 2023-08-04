from injector import Injector




from application.services.ContextService import ContextService

from adapter.out.persistence.contextRepository import ContextRepository
from adapter.out.persistence.binaryQuestionRepository import BinaryQuestionRepository
from adapter.In.controllers.ContextController import ContextController

injector = Injector()

contextRepository = injector.get(ContextRepository)
contextService = injector.get(ContextService)
binaryQuestionRepository = injector.get(BinaryQuestionRepository)
contextController = injector.get(ContextController)






