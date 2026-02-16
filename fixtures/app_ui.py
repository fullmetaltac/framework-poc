import pytest

from core.app.ui.ui_client import UI
from core.env import BASE_UI_URL, CI


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": CI,
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
    }


# @pytest.fixture(scope="session")
# def storage_state(tmp_path_factory, browser):
#     auth_dir = tmp_path_factory.mktemp("auth")
#     state_file = auth_dir / "state.json"

#     context = browser.new_context()
#     page = context.new_page()

#     page.goto(BASE_UI_URL, wait_until="domcontentloaded")
#     # LOGIN STEPS
#     context.storage_state(path=state_file)
#     context.close()

#     return str(state_file)


# @pytest.fixture(scope="function")
# def context(browser, storage_state):
#     context = browser.new_context(storage_state=storage_state)
#     yield context
#     context.close()


@pytest.fixture
def ui(page, logger) -> UI:
    page.goto(BASE_UI_URL)
    return UI(page, logger)
