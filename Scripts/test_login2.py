from Base.get_driver import get_driver
from Page.login_page import LoginPage


class aTestLogin:
    """测试登录脚本类"""

    def setup_class(self):
        self.login_page = LoginPage(get_driver())

    def teardown_class(self):
        self.login_page.driver.quit()

    def atest_login_case(self):
        self.login_page.page_input_username("18210783786")
        self.login_page.page_input_passwd("123456")
        self.login_page.page_login_click()

    def test_haha(self):
        pass
