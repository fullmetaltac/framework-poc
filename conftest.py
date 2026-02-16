import pytest

from core.env import LOGS_DIR, SCREENSHOTS_DIR
from core.utils.util_file_system import delete_outdated_files, screenshot_path, test_id


@pytest.fixture(scope="session", autouse=True)
def global_setup_teardown():
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    delete_outdated_files()
    yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):  # pylint: disable=W0613
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        if page := item.funcargs.get("page"):
            _id = test_id(item.get_closest_marker("case"))
            page.screenshot(path=screenshot_path(item.name, _id))


pytest_plugins = [
    "fixtures.app_api",
    "fixtures.app_ui",
    "fixtures.logger",
]
