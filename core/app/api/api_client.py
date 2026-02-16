from core.app.api.api_session import ApiSession
from core.app.api.steps.steps_company import CompanyActions
from core.app.api.steps.steps_user import UserActions


class API:
    def __init__(self, session: ApiSession):
        self.user: UserActions = UserActions(session)
        self.company: CompanyActions = CompanyActions(session)
