import pytest
from playwright.sync_api import Page, Browser, Playwright


@pytest.fixture(scope="function")
def page(browser: Browser) -> Page:
    """创建新的页面实例"""
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="session")
def playwright_instance():
    """Playwright 实例"""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance):
    """浏览器实例"""
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=500)
    yield browser
    browser.close()