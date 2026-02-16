from typing import Self

from core.app.ui.page_base import BasePage


class MainPage(BasePage):

    # Selectors

    search_bar = ".DocSearch"

    # Actions

    def open_search(self) -> Self:
        self.page.click(self.search_bar)
        return self
