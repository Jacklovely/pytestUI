import allure
import pytest
from common.log import Log
from common.read_yml import ReadYaml
from pages.login_page import LoginPage
from selenium import webdriver
testdata = ReadYaml('login_page.yml').get_yaml_data()#读取数据

class Test_login():

    log = Log()

    @allure.feature("功能点：用户登录页面")
    @allure.story("用例：用户登录")
    @pytest.mark.parametrize("username,password,msg",testdata["test_login_success_data"],
                             ids = ["正确用户名密码登录"])
    @pytest.mark.skip('跳过该成功用例')
    def test_success_login(self,driver,username,password,msg):
        #driver = webdriver.Chrome()
        web = LoginPage(driver)
        web.login(user=username,password=password)
        result = web.is_login_success(expect_text=msg)
        self.log.info("登录结果：%s"%result)
        assert result
        #driver.quit()

    @allure.feature("功能点：用户登录页面")
    @allure.story("用例：用户登录")
    @pytest.mark.parametrize("username,password,msg", testdata["test_login_fail_data"],
                             ids=["正确用户名错误密码登录",
                                  "错误用户名正确密码登录"])
    def test_fail_login(self,driver,username,password,msg):
        #driver = webdriver.Chrome()
        web = LoginPage(driver)
        web.login(user=username,password=password)
        result = web.is_login_fail(expect_text=msg)
        self.log.info("登录结果:%s"%result)
        assert result
