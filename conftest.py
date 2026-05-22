import pytest
from playwright.sync_api import Page, Browser, Playwright, sync_playwright

@pytest.fixture(scope="function")
def page(browser_context):
    """创建新页面并返回"""
    page = browser_context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="function")
def browser_context():
    """创建浏览器上下文，注意：由于登录弹窗是每次访问出现的，
    所以使用function级别的context即可，不需要持久化登录状态"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)  # 方便观察，可改为True
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        yield context
        context.close()
        browser.close()