from playwright.sync_api import Page, Locator
from typing import List


class SuggestionComponent:
    """搜索建议下拉框可复用组件"""

    def __init__(self, page: Page):
        self.page = page
        self._suggestion_list: Locator = page.locator("#form .bdsug-new ul li")
        self._suggestion_items: Locator = page.locator("#form .bdsug-new ul li a")

    def is_visible(self) -> bool:
        """检查搜索建议是否可见"""
        return self._suggestion_list.first.is_visible() if self._suggestion_list.count() > 0 else False

    def get_suggestion_texts(self) -> List[str]:
        """获取所有搜索建议的文本"""
        if not self.is_visible():
            return []
        return self._suggestion_list.all_inner_texts()

    def get_suggestion_count(self) -> int:
        """获取搜索建议数量"""
        return self._suggestion_list.count()

    def click_suggestion_by_index(self, index: int) -> None:
        """点击第几个搜索建议"""
        suggestions = self._suggestion_list.all()
        if 0 <= index < len(suggestions):
            suggestions[index].click()

    def click_suggestion_by_text(self, text: str) -> bool:
        """通过文本点击搜索建议"""
        for suggestion in self._suggestion_items.all():
            if text in suggestion.inner_text():
                suggestion.click()
                return True
        return False

    def wait_for_suggestions(self, timeout: int = 5000):
        """等待搜索建议出现"""
        self.page.wait_for_selector("#form .bdsug-new ul li", state="visible", timeout=timeout)