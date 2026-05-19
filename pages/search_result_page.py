from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class SearchResultPage(BasePage):
    """搜索结果页 Page Object"""

    def __init__(self, page: Page):
        super().__init__(page)

        # 搜索结果定位器
        self._result_links: Locator = page.locator("#content_left h3 a")
        self._result_titles: Locator = page.locator("#content_left h3")
        self._search_input: Locator = page.locator("#kw")
        self._search_button: Locator = page.locator("#su")
        self._result_stats: Locator = page.locator(".nums_text")

    def get_result_titles(self) -> list[str]:
        """获取所有搜索结果的标题"""
        return self._result_titles.all_inner_texts()

    def get_result_links(self, limit: int = 10) -> list[str]:
        """获取搜索结果链接"""
        links = self._result_links.all()
        return [link.get_attribute("href") for link in links[:limit] if link.get_attribute("href")]

    def click_result_by_index(self, index: int) -> None:
        """点击第几个搜索结果"""
        results = self._result_links.all()
        if 0 <= index < len(results):
            results[index].click()

    def get_result_count_text(self) -> str:
        """获取搜索结果统计信息"""
        if self._result_stats.count() > 0:
            return self._result_stats.first.inner_text()
        return ""

    def is_search_result_present(self) -> bool:
        """检查是否有搜索结果"""
        return self._result_links.count() > 0