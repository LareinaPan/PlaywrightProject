from playwright.sync_api import Page, Locator


class SearchInputComponent:
    """搜索输入框可复用组件"""

    def __init__(self, page: Page):
        self.page = page
        self._input: Locator = page.locator("#kw")
        self._clear_icon: Locator = page.locator("#kw + span .soutu-clear-icon")

    def input_text(self, text: str) -> "SearchInputComponent":
        """输入搜索文本"""
        self._input.fill(text)
        return self

    def clear_text(self) -> "SearchInputComponent":
        """清空输入框"""
        self._input.clear()
        return self

    def get_text(self) -> str:
        """获取输入框中的文本"""
        return self._input.input_value()

    def press_enter(self) -> None:
        """按回车键"""
        self._input.press("Enter")

    def is_focused(self) -> bool:
        """检查输入框是否获得焦点"""
        return self._input.evaluate("el => el === document.activeElement")

    def type_slowly(self, text: str, delay: int = 100) -> "SearchInputComponent":
        """模拟慢速输入"""
        self._input.type(text, delay=delay)
        return self