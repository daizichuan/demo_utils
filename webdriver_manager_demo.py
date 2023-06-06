import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # Chrome
from webdriver_manager.firefox import GeckoDriverManager  # FireFox
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager  # IE、Edge

base_url = "https://www.baidu.com"

driver = webdriver.Chrome(ChromeDriverManager().install())  # Chrome
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())  # FireFox
# driver = webdriver.Ie(IEDriverManager().install())  # IE
# driver = webdriver.Edge(EdgeChromiumDriverManager().install())  # Edge

driver.get(base_url)

driver.implicitly_wait(3)

element_kw = driver.find_element(by=By.ID, value='kw')
element_kw.send_keys('python')

element_btn = driver.find_element(by=By.ID, value='su')
element_btn.click()

time.sleep(3)

driver.quit()
