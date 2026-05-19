import re

import pytest
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://www.baidu.com", timeout=30000)
    expect(page).to_have_title(re.compile("百度一下"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

@pytest.fixture(scope="function")
def before_each_after_each(page: Page):
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://playwright.dev/")
    yield

    print("after the test runs")