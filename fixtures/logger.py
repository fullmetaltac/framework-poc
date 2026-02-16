from logging import DEBUG, INFO, FileHandler, Formatter, getLogger

import pytest
from pytest import FixtureRequest

from core.utils.util_file_system import log_path, test_name


@pytest.fixture
def logger(request: FixtureRequest):
    api_logger = getLogger(test_name(request))
    api_logger.setLevel(DEBUG)

    file_name = log_path(request)
    handler = FileHandler(file_name, mode="w", encoding="utf-8")
    handler.setLevel(INFO)

    formatter = Formatter("%(asctime)s %(message)s")
    handler.setFormatter(formatter)
    api_logger.addHandler(handler)

    yield api_logger

    api_logger.removeHandler(handler)
    handler.close()
