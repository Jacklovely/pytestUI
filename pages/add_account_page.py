from common.base import Base
from common.read_yml import ReadYaml
testelement = ReadYaml("add_account_page.yml").get_yaml_data()

class Add_Account(Base):

    loc1 = tuple(testelement["test_account_element"][0])  # 银行卡账户
    loc2 = tuple(testelement["test_account_element"][1])  # 添加银行卡账户
    loc3 = tuple(testelement["test_account_element"][2])  # 卡号
    loc4 = tuple(testelement["test_account_element"][3])  # 姓名
    loc5 = tuple(testelement["test_account_element"][4])  # 电话
    loc6 = tuple(testelement["test_account_element"][5])  # 邮箱
    loc7 = tuple(testelement["test_account_element"][6])  # 城市
    loc8 = tuple(testelement["test_account_element"][7])  # 性别
    loc9 = tuple(testelement["test_account_element"][8])  # 保存
    loc10 = tuple(testelement["test_account_element"][9]) # 新增成功校验
    loc11 = tuple(testelement["test_account_element"][10]) #账号为空校验
    loc12 = tuple(testelement["test_account_element"][11]) #姓名为空校验

    def click_account(self):
        '''点击银行卡账号'''
        self.finds(self.loc1)[0].click()

    def click_add_account(self):
        '''点击添加银行卡账号'''
        self.click(self.loc2)

    def input_card_num(self,text = "123456"):
        '''输入卡号'''
        self.writein(self.loc3,text)

    def input_name(self,text = " "):
        '''输入姓名'''
        self.writein(self.loc4,text)

    def input_phone(self,text = "123456"):
        '''输入电话'''
        self.writein(self.loc5,text)

    def input_mail(self,text = "123456"):
        '''输入邮箱'''
        self.writein(self.loc6,text)

    def input_city(self,text = "测试"):
        '''输入城市'''
        self.writein(self.loc7,text)

    def input_sex(self,text = "男"):
        '''输入性别'''
        self.writein(self.loc8,text)

    def click_save(self):
        '''点击保存'''
        self.click(self.loc9)

    def is_add_success(self, expect_text='添加成功'):
        text = self.get_text(self.loc10)
        self.log.info("获取到断言元素的文本内容：%s" %text)
        return expect_text in text

    def is_add_fail1(self, expect_text='这个字段是必须的'):
        '''账号为空断言'''
        text = self.get_text(self.loc11)
        self.log.info("获取到断言元素的文本内容：%s" % text)
        return expect_text in text

    def is_add_fail2(self, expect_text='这个字段是必须的'):
        '''姓名为空断言'''
        text = self.get_text(self.loc12)
        self.log.info("获取到断言元素的文本内容：%s" % text)
        return expect_text in text

    def is_add_fail2(self, expect_text='这个字段是必须的'):
        '''姓名为空断言'''
        text = self.get_text(self.loc12)
        self.log.info("获取到断言元素的文本内容：%s" %text)
        return expect_text in text

if __name__ == '__main__':
    from pages.login_page import LoginPage
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    web = LoginPage(driver)
    web.login()
    account = Add_Account(driver)
    account.click_account()
    account.click_add_account()
    account.input_card_num()
    account.input_name()
    account.input_phone()
    account.input_mail()
    account.input_city()
    account.input_sex()
    account.click_save()
    account.is_add_fail()
    driver.quit()
    


