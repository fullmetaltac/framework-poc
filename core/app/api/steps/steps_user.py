from core.app.api.api_session import ApiSession
from core.app.api.clients.api_user import UserService
from core.models.model_user import UserDC


class UserActions:
    def __init__(self, session: ApiSession):
        self.api: UserService = UserService(session)

    def get_user(self, data: UserDC) -> UserDC:
        res = self.api.get_user(data).validate_status()
        return UserDC.model_validate(res.json()["args"])
