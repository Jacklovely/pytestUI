from selenium import webdriver
from pages.login_page import LoginPage
import pytest
import time
from selenium.webdriver.chrome.options import Options
@pytest.fixture(scope="session")
def login_fixtrue():
    #登录前置操作
    driver = webdriver.Chrome()
    driver.maximize_window()
    web = LoginPage(driver)
    web.login()
    return driver
def pytest_addoption(parser):
    '''添加命令行参数'''
    parser.addoption('--headless', action = "store",
                     default = 'no', help = 'set chrome headless option yes or no'
    )
@pytest.fixture(scope="session")
def driver(request):
    """定义全局driver fixture，给其它地方作参数调用"""
    headless = request.config.getoption("--headless")
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')# 设置当前窗口的宽度和高度
    if headless=="yes":
        chrome_options.add_argument('--headless')  # 无界面
    _driver = webdriver.Chrome(chrome_options=chrome_options)

    def end():
        print("全部用例执行完后 teardown quit dirver")
        time.sleep(5)
        _driver.quit()
        request.addfinalizer(end)
        return _driver
