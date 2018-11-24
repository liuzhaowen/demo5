from selenium.webdriver.common.by import By

from Base.base import Base


user_name_el = By.ID, "android:id/statusBarBackground"
pass_word_el = By.ID, "com.vcooline.aike:id/etxt_pwd"
login_btn_el = By.ID, "com.vcooline.aike:id/btn_login"


class LoginPage(Base):

    # 输入用户名
    def page_input_username(self, user_name):
        self.base_input_element(user_name_el, user_name)

    # 输入密码
    def page_input_passwd(self, passwd):
        self.base_input_element(pass_word_el, passwd)

    # 点击登录
    def page_login_click(self):
        self.base_click_element(login_btn_el)
