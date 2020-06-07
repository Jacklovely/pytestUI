import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def login_fixtrue():
    #登录前置操作
    driver = webdriver.Chrome
    driver.maximize_window()
    web=LoginPage(driver)
    web.login()
    return driver