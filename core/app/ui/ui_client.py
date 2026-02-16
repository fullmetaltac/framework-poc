from logging import Logger

from playwright.sync_api import Page

from core.app.ui.components.component_searchbar import SearchBar
from core.app.ui.pages.page_main import MainPage


class UI:

    def __init__(self, page: Page, logger: Logger):
        self.page: Page = page
        self.logger: Logger = logger

        # Pages
        self.main_page = MainPage(page, logger)

        # Components
        self.search_bar = SearchBar(page, logger)
