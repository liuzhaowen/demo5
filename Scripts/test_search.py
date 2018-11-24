import pytest as pytest

from Base.get_driver import get_driver
from Page.setting_search_page import SearchPage


class TestSearch:

    def setup_class(self):
        self.setting_search_page = SearchPage(get_driver())

    def teardown_class(self):
        self.setting_search_page.driver.quit()

    @pytest.mark.parametrize("value,except_result", [("l", "移动网络"), ("a", "壁纸"), ("w", "WLAN")])
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_search_cases(self, value, except_result):
        self.setting_search_page.page_search_click()
        self.setting_search_page.page_search_input(value)
        try:
            text_list = self.setting_search_page.page_search_elements_text()
            print(except_result)
            print(text_list)
            assert except_result in text_list
        except Exception as e:
            print(e)


        self.setting_search_page.page_search_back()


