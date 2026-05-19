from playwright.sync_api import Page
from typing import Optional


class BasePage:
    """页面基类"""

    def __init__(self, page: Page):
        self.page = page

    def wait_for_element(self, selector: str, timeout: int = 30000):
        """等待元素出现"""
        self.page.wait_for_selector(selector, state="visible", timeout=timeout)

    def take_screenshot(self, name: str = "screenshot.png"):
        """截图"""
        self.page.screenshot(path=name)

    def get_current_url(self) -> str:
        """获取当前URL"""
        return self.page.url