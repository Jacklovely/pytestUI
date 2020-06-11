import platform
import sys

from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
def is_windows_linux():
    '''判断当前系统是windows还是linux:
    一般linux结果为('32bit','ELF')ELF或者('64bit','ELF')ELF,
    windows为（'32bit','windowsPE'）,或者（'64bit','windowsPE'）'''
    if platform.system()=='Windows':
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度，高度
        chrome_options.add_argument('--headless')  # 无界面
        print("当前运行的操作系统为windows")
        driver = webdriver.Chrome(chrome_options=chrome_options)
    else:
        print('当前运行的操作系统为linux')
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度，高度
        chrome_options.add_argument('--no-sandbox')#解决DevToolsActivePort文件不存在报错问题
        chrome_options.add_argument('--disable-gpu')#禁用GPU硬件加速，如果软件渲染器没有就位，则GPU进程将不会启动
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')  # 无界面
        driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver
driver = is_windows_linux()
driver.get("https://www,baidu.com")
driver.quit()
