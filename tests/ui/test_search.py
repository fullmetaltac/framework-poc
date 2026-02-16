import pytest
from assertpy import assert_that

from core.app.api.api_client import API
from core.app.ui.ui_client import UI
from core.models.model_user import UserDC


@pytest.mark.case("BG-333333")
@pytest.mark.parametrize("user_data", [UserDC(name="aqa-user", email="aqa@gmail.com")])
def test_search(ui: UI, api: API, user_data: UserDC):
    api.user.get_user(user_data)
    ui.main_page.open_search()
    ui.search_bar.search_doc("WebView2")

    assert_that(ui.search_bar.is_item_present("WebView2"))
