from playwright.sync_api import Page, Locator
from pages.base_page import BasePage
from components.search_input_component import SearchInputComponent
from components.suggestion_component import SuggestionComponent


class BaiduHomePage(BasePage):
    """百度首页 Page Object"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = "https://www.baidu.com"

        # 页面元素定位器
        self._logo: Locator = page.locator("#lg")
        self._search_button: Locator = page.locator("#su")
        self._setting_link: Locator = page.locator("#s-usersetting-top")

        # 可复用组件
        self.search_input = SearchInputComponent(page)
        self.suggestion = SuggestionComponent(page)

    def navigate_to_baidu(self) -> "BaiduHomePage":
        """导航到百度首页"""
        self.page.goto(self.url)
        self.wait_for_page_load()
        return self

    def search(self, keyword: str) -> "BaiduHomePage":
        """执行搜索"""
        self.search_input.input_text(keyword)
        self.search_input.press_enter()
        return self

    def search_by_click(self, keyword: str) -> "BaiduHomePage":
        """通过点击按钮搜索"""
        self.search_input.input_text(keyword)
        self._search_button.click()
        return self

    def get_suggestion_texts(self) -> list[str]:
        """获取搜索建议文本列表"""
        return self.suggestion.get_suggestion_texts()

    def is_logo_visible(self) -> bool:
        """检查百度Logo是否可见"""
        return self._logo.is_visible()

    def get_page_title(self) -> str:
        """获取页面标题"""
        return self.page.title()

    def wait_for_page_load(self):
        """等待页面加载完成"""
        self.page.wait_for_selector("#kw", state="visible")
        self.page.wait_for_selector("#su", state="visible")