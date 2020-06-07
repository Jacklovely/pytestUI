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
    loc10 = tuple(testelement["test_account_element"][9]) # 校验



