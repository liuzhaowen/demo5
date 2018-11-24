# 服务端启动参数
from appium import webdriver


def get_driver():
    desired_caps = {}
    # 手机 系统信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    # 设备号
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 包名
    desired_caps['appPackage'] = 'com.android.settings'
    # desired_caps['appPackage'] = 'com.vcooline.aike'
    # 启动名
    desired_caps['appActivity'] = '.Settings'
    # desired_caps['appActivity'] = '.umanager.LoginActivity'
    # 允许输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 手机驱动对象
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver