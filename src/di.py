from injector import Injector




from application.services.ContextService import ContextService
from application.services.UserService import UserService

from adapter.out.persistence.contextRepository import ContextRepository
from adapter.In.controllers.ContextController import ContextController
from adapter.In.controllers.UserController import UserController

injector = Injector()

contextRepository = injector.get(ContextRepository)
contextService = injector.get(ContextService)
contextController = injector.get(ContextController)
userService = injector.get(UserService)
userController = injector.get(UserController)






