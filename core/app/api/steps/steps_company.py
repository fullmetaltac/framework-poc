from core.app.api.api_session import ApiSession
from core.app.api.clients.api_company import CompanyService
from core.models.model_company import CompanyDC


class CompanyActions:
    def __init__(self, session: ApiSession):
        self.api: CompanyService = CompanyService(session)

    def get_company(self, data: CompanyDC) -> CompanyDC:
        res = self.api.get_company(data).validate_status()
        return CompanyDC.model_validate(res.json()["args"])
