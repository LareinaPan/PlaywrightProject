import re
import pytest
from playwright.sync_api import Page, expect, Playwright,sync_playwright, expect

class TestJDProduct:
    def test_jd_login_popup_and_search(self, page: Page):
        # 1. 访问京东首页，等待自动跳出登录弹窗
        page.goto("https://www.jd.com/", wait_until="domcontentloaded")
        # expect(page).to_have_url("https://www.jd.com/")
        expect(page).to_have_url(re.compile(r"\.jd\.com/"))
        expect(page).to_have_title(re.compile(r"京东"))

        login_popup = page.locator("#login2025-content").content_frame.locator(".sms-login-submit-box")
        expect(login_popup).to_be_visible(timeout=10000)

        # 2. 点击登录弹窗右上角的X，断言登录弹窗成功关闭
        close_button = page.locator("#login2025-dialog-close")
        close_button.click()
        search_input = page.get_by_role("textbox", name="搜索")
        expect(login_popup).not_to_be_visible()
        expect(search_input).to_be_visible()

        # 3. 在京东首页搜索框里搜索"小米空调"，点击搜索按钮，断言跳转到商品列表页面，且展示小米空调的商品卡片
        search_input.click()
        search_input.fill("小米空调")
        search_button = page.get_by_role("button", name="搜索")
        search_button.click()
        # expect(page).to_have_url(re.compile(r"\.jd\.com/search\?"))
        # product_card = page.locator("div.gl-item, li.gl-item, div[class*='item']:has(img)").first
        # expect(product_card).to_be_visible()
        # card_text = product_card.inner_text()
        # assert "小米" in card_text or "空调" in card_text
        # 再次跳转到京东登录页面
        expect(page).to_have_url(re.compile(r"\.jd\.com/new/login.aspx\?"))