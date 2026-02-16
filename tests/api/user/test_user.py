import pytest
from assertpy import assert_that

from core.app.api.api_client import API
from core.models.model_user import UserDC


@pytest.mark.case("BG-22222")
@pytest.mark.parametrize("user_data", [UserDC(name="aqa-user", email="aqa@gmail.com")])
def test_user(api: API, user_data: UserDC):
    user = api.user.get_user(user_data)

    assert_that(user.name).is_not_empty()
    assert_that(user.email).is_not_empty()
