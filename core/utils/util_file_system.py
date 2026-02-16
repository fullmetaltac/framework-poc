from datetime import datetime, timedelta
from pathlib import Path

from pytest import FixtureRequest, Mark

from core.env import LOGS_DIR, SCREENSHOTS_DIR, TEMP_DIR
from core.utils.util_exceptions import TestIdRequired
from core.utils.util_time import ts


def test_name(request: FixtureRequest) -> str:
    return request.node.nodeid.split("::")[-1]


def test_id(mark: Mark) -> str:
    if mark:
        return mark.args[0]
    raise TestIdRequired()


def log_path(request: FixtureRequest) -> Path:
    mark = request.node.get_closest_marker("case")
    return LOGS_DIR / f"{test_name(request)}[{test_id(mark)}].txt"


def screenshot_path(name: str, test_id: str) -> Path:
    return SCREENSHOTS_DIR / f"{name}-[{test_id}]-{ts()}.png"


def delete_outdated_files(days: int = 1):
    today = datetime.now().date()
    yesterday = today - timedelta(days=days)

    for file in TEMP_DIR.rglob("*"):
        if file.is_file():
            mtime = file.stat().st_mtime
            file_date = datetime.fromtimestamp(mtime).date()
            if file_date == yesterday:
                file.unlink()
