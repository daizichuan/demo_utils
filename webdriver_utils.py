import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager

'''
1、使用文档
https://pypi.org/project/webdriver-manager/
2、page_load_strategy 设置说明
normal：等待整个页面加载完毕再开始执行操作
eager：等待整个dom树加载完成，即DOMContentLoaded这个事件完成，也就是只要 HTML 完全加载和解析完毕就开始执行操作。放弃等待图片、样式、子帧的加载。
none：等待html下载完成，哪怕还没开始解析就开始执行操作。
3、implicitly_wait
设置全局隐性等待时间，单位：秒
'''


def gen_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-error")
    options.add_argument("--ignore-ssl-errors")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver


def gen_ie_driver():
    options = webdriver.IeOptions()
    # 无头某事，不显示浏览器
    # options.add_argument('--headless')
    # 忽略浏览器存在缩放而出现的错误信息。
    options.ignore_zoom_level = True
    # 忽略警告
    options.ignore_protected_mode_settings = True
    # 加载策略
    options.page_load_strategy = 'none'
    driver = webdriver.Ie(service=IEService(IEDriverManager(cache_valid_range=7).install()), options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver


selenium_Driver = gen_ie_driver
generate_driver = gen_ie_driver
seleniumDriver_chrome = gen_chrome_driver

if __name__ == '__main__':
    # driver = gen_chrome_driver()
    # driver = gen_ie_driver()
    # driver = selenium_Driver()
    # driver = generate_driver()
    driver = seleniumDriver_chrome()
    driver.get('https://www.baidu.com/')
    time.sleep(2)
    driver.quit()
