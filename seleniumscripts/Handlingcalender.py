import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.goibibo.com/")
time.sleep(2)
driver.find_element(By.XPATH,'//span[@class="sc-iCfMLu ixvMbU"]').click()
driver.find_element(By.XPATH,'//span[text()="Departure"]').click()
dates=driver.find_elements(By.XPATH,'(//div[@class="DayPicker-Body"])[1]//div//p[@class="fsw__date"]')
print(len(dates))
for date in dates:
    print(date.text)
    if '15' in date.text:
        date.click()
        # time.sleep(3)
        continue
driver.execute_script("scroll(0, 0);")
time.sleep(3)
driver.find_element(By.XPATH,'//div[@class="gr_fswFld"]').click()
time.sleep(3)
todates=driver.find_elements(By.XPATH,'(//div[@class="DayPicker-Body"])[1]//div//p[@class="fsw__date"]')
for d in todates:
    if '18' in d.text:
        d.click()
        time.sleep(4)
driver.find_element(By.XPATH,'//span[text()="Done"]').click()