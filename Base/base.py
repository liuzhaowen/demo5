from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    """定义一个基类"""

    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def base_find_element(self, loc, time_out=10, poll_fre=0.5):
        element = WebDriverWait(self.driver, time_out, poll_fre).until(lambda x:x.find_element(*loc))
        # element = self.driver.find_element(*loc)
        return element

    # 点击元素
    def base_click_element(self, loc):
        self.base_find_element(loc).click()

    # 输入元素
    def base_input_element(self, loc, text_input):
        self.base_find_element(loc).clear().send_keys(text_input)

    # 定位一组元素
    def base_find_elements(self, loc, time_out=10, poll_fre=0.5):
        elements = WebDriverWait(self.driver, time_out, poll_fre).until(lambda x:x.find_elements(*loc))
        return elements


