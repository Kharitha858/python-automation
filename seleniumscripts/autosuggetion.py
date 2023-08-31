import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.goibibo.com/")
time.sleep(2)
driver.find_element(By.XPATH,'//div[@class="sc-12foipm-16 dwhdnN fswFld "]//span[text()="From"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//div[@class="sc-12foipm-34 dVpEne"]//div//input[@type="text"]').send_keys("Vi")
time.sleep(3)
webelements=driver.find_elements(By.XPATH,'//ul[@id="autoSuggest-list"]//li')
print(len(webelements))
for ele in webelements:
    print("places:",ele.text)
    if 'Vinh City, Vietnam' in ele.text:
        print("place found")
        ele.click()
        time.sleep(3)
        break
