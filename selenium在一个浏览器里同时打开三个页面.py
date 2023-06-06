# coding=utf-8
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

website = "www.baidu.com"

js = "window.open('{}','_blank');"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)



driver.get(f'http://xxx/#/index?url={website}')
time.sleep(0.2)
driver.execute_script(js.format(f'https://{website}'))
time.sleep(0.2)
driver.execute_script(js.format(f'https://xxx/{website}?domain={website}&status=q'))
time.sleep(0.2)
driver.switch_to.window(driver.window_handles[-1])

time.sleep(10)

driver.quit()
