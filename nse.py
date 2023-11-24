import time

from selenium_programs import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.nseindia.com/')
driver.maximize_window()
driver.find_element("xpath",'//a[text()="Market Data"]').click()
# time.sleep(6)
driver.find_element("xpath",'(//a[text()="Indices"])[1]').click()
time.sleep(4)