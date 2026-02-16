from core.app.api.api_response import ApiResponse
from core.app.api.api_session import ApiSession
from core.env import BASE_API_URL
from core.models.model_user import UserDC


class UserService:
    def __init__(self, session: ApiSession):
        self.session = session

    def get_user(self, data: UserDC) -> ApiResponse:
        return self.session.request("GET", f"{BASE_API_URL}/get?name={data.name}&email={data.email}")
