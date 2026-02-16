import pytest
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from core.app.api.api_client import API
from core.app.api.api_session import ApiSession


@pytest.fixture
def session(logger):
    session = ApiSession(logger)
    # auth step here

    retry_strategy = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    yield session
    session.close()


@pytest.fixture
def api(session) -> API:
    return API(session)
