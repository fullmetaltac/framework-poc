from typing import Self

from core.app.ui.page_base import BasePage


class SearchBar(BasePage):

    # Selectors

    search_input = "#docsearch-input"
    search_item = "//*[contains(text(), '{name}')]"

    # Actions

    def search_doc(self, name: str) -> Self:
        self.page.fill(self.search_input, name)
        return self

    # State

    def is_item_present(self, name: str):
        return self.page.is_visible(self.search_item.format(name=name))
