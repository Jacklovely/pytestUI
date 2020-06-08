import allure
import pytest
from common.log import Log
from common.read_yml import ReadYaml
from pages.add_account_page import Add_Account
testdata = ReadYaml('add_account_page.yml').get_yaml_data()#读取测试数据

class Test_Add_Account():
    log = Log()

    @allure.feature("功能点：添加银行卡账户")
    @allure.story("用例：添加银行卡账户")
    @pytest.mark.parametrize("card_num,name,phone,mail,city,sex,msg",testdata["test_add_account_data"],
                             ids=["正常添加"])
    def test_add_account(self, login_fixtrue,card_num, name, phone,mail,city,sex,msg):
        driver = login_fixtrue
        account = Add_Account(driver)
        with allure.step("点击银行卡账户，跳转添加账户页面"):
            account.click_account()
        with allure.step("点击添加账户按钮，进入编辑页面"):
            account.click_add_account()
        with allure.step("输入账户号"):
            account.input_card_num(text=card_num)
        with allure.step("输入姓名"):
            account.input_name(text=name)
        with allure.step("输入手机号"):
            account.input_phone(text=phone)
        with allure.step("输入邮箱"):
            account.input_mail(text=mail)
        with allure.step("输入城市"):
            account.input_city(text=city)
        with allure.step("输入性别"):
            account.input_sex(text=sex)
        with allure.step("点击保存"):
            account.click_save()
        with allure.step("获取结果: 获取页面实际结果，判断是否添加成功"):
            result = account.is_add_success(expect_text=msg)
            self.log.info("登录结果：%s"%result)
        with allure.step("断言：判断是否添加成功"):
            assert result == True
        driver.quit()



