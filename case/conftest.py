import os
import platform

import allure
from selenium import webdriver
from pages.login_page import LoginPage
import pytest
import time
from common.log import Log
from selenium.webdriver.chrome.options import Options
log = Log()

_driver = None
@pytest.fixture(scope="session")
def login_fixtrue(browser):
    #登录前置操作
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    web = LoginPage(_driver)
    web.login()
    return _driver

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(_driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)

def pytest_addoption(parser):
    '''添加命令行参数'''
    parser.addoption('--headless', action = "store",
                     default = 'no', help = 'set chrome headless option yes or no'
    )
@pytest.fixture(scope="session")
def driver(request):
    """定义全局driver fixture，给其它地方作参数调用"""
    if platform.system()=='Windows':
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度，高度
        chrome_options.add_argument('--headless')  # 无界面
        log.info("当前运行的操作系统为windows")
        _driver = webdriver.Chrome(options=chrome_options)
    else:
        log.info('当前运行的操作系统为linux')
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度，高度
        chrome_options.add_argument('--no-sandbox')#解决DevToolsActivePort文件不存在报错问题
        chrome_options.add_argument('--disable-gpu')#禁用GPU硬件加速，如果软件渲染器没有就位，则GPU进程将不会启动
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')  # 无界面
        _driver = webdriver.Chrome(options=chrome_options)

    def end():
        log.info("全部用例执行完后 teardown quit dirver")
        time.sleep(5)
        _driver.quit()
    request.addfinalizer(end)
    return _driver

@pytest.fixture(scope='session')
def browser():
    global _driver
    if _driver is None:
        _driver =webdriver.Chrome()
    yield _driver
    print("1111111111")
    _driver.quit()