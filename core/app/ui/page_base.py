from functools import wraps
from logging import Logger

from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page, logger: Logger):
        self.page: Page = page
        self.logger: Logger = logger

    def __getattribute__(self, name):
        """
        Logging each function call inside the class
        """
        attr = super().__getattribute__(name)

        if callable(attr) and not name.startswith("_"):

            @wraps(attr)
            def wrapper(*args, **kwargs):
                self.logger.info(f"[{self.__class__.__name__}] → {name}")
                return attr(*args, **kwargs)

            return wrapper

        return attr
