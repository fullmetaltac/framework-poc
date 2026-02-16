from core.app.api.api_response import ApiResponse
from core.app.api.api_session import ApiSession
from core.env import BASE_API_URL
from core.models.model_company import CompanyDC


class CompanyService:
    def __init__(self, session: ApiSession):
        self.session = session

    def get_company(self, data: CompanyDC) -> ApiResponse:
        return self.session.request("GET", f"{BASE_API_URL}/get?name={data.name}&location={data.location}")
