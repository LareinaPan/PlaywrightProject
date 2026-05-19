import pytest
from pages.baidu_home_page import BaiduHomePage
from pages.search_result_page import SearchResultPage


class TestBaiduSearch:
    """百度搜索测试类"""

    def test_baidu_homepage_load(self, page):
        """测试百度首页加载"""
        home_page = BaiduHomePage(page)
        home_page.navigate_to_baidu()

        # 断言
        assert "百度" in home_page.get_page_title()
        assert home_page.is_logo_visible()
        assert home_page.search_input.is_focused()

    def test_search_functionality(self, page):
        """测试搜索功能"""
        home_page = BaiduHomePage(page)
        home_page.navigate_to_baidu()

        # 执行搜索
        keyword = "Playwright"
        home_page.search(keyword)

        # 验证搜索结果
        result_page = SearchResultPage(page)
        assert result_page.is_search_result_present()

        titles = result_page.get_result_titles()
        assert any(keyword.lower() in title.lower() for title in titles)

    def test_search_suggestions(self, page):
        """测试搜索建议功能"""
        home_page = BaiduHomePage(page)
        home_page.navigate_to_baidu()

        # 输入部分关键词
        partial_keyword = "play"
        home_page.search_input.input_text(partial_keyword)

        # 等待建议出现
        home_page.suggestion.wait_for_suggestions()

        # 验证建议
        suggestions = home_page.get_suggestion_texts()
        assert len(suggestions) > 0
        assert any(partial_keyword in suggestion.lower() for suggestion in suggestions)

    def test_search_by_click_button(self, page):
        """测试通过点击按钮搜索"""
        home_page = BaiduHomePage(page)
        home_page.navigate_to_baidu()

        keyword = "Python Playwright"
        home_page.search_by_click(keyword)

        result_page = SearchResultPage(page)
        assert result_page.is_search_result_present()

    def test_empty_search(self, page):
        """测试空搜索"""
        home_page = BaiduHomePage(page)
        home_page.navigate_to_baidu()

        # 不输入内容直接搜索
        home_page.search_input.press_enter()

        # 验证仍在百度首页
        assert "百度" in home_page.get_page_title()
        assert home_page.search_input.get_text() == ""

    def test_search_result_click(self, page):
        """测试点击搜索结果"""
        home_page = BaiduHomePage(page)
        home_page.navigate_to_baidu()

        # 执行搜索
        home_page.search("Playwright Python")

        # 点击第一个搜索结果
        result_page = SearchResultPage(page)
        initial_url = page.url

        result_page.click_result_by_index(0)

        # 验证页面跳转
        page.wait_for_load_state()
        assert page.url != initial_url

    @pytest.mark.parametrize("keyword", [
        "pytest",
        "selenium",
        "自动化测试"
    ])
    def test_multiple_keywords(self, page, keyword):
        """参数化测试多个关键词"""
        home_page = BaiduHomePage(page)
        home_page.navigate_to_baidu()

        home_page.search(keyword)

        result_page = SearchResultPage(page)
        assert result_page.is_search_result_present()
        assert keyword in page.url or keyword in result_page.get_result_titles()[0]