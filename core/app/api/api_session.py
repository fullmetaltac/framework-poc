from logging import Logger

from requests import Session

from core.app.api.api_response import ApiResponse
from core.env import TIMEOUT_API
from core.utils.util_logger import log_api


class ApiSession(Session):
    def __init__(self, logger: Logger):
        super().__init__()
        self.logger = logger

    def request(self, method, url, **kw):
        kw.setdefault("timeout", TIMEOUT_API)
        res = super().request(method, url, **kw)
        log_api(self.logger, res)
        return ApiResponse(res)
