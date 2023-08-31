import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.flipkart.com/')
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element(By.XPATH,'//button[text()="✕"]').click()
driver.find_element(By.XPATH,'//div[@class="col-12-12 _2oO9oE"]').click()
driver.find_element(By.XPATH,'//input[@title="Search for products, brands and more"]').send_keys('Oneplus mobiles')
driver.find_element(By.XPATH,'//button[@class="L0Z3Pu"]').click()

time.sleep(3)
parentwindow=driver.current_window_handle
print(parentwindow)
driver.find_element(By.XPATH,'//div[text()="OnePlus"]').click()
driver.find_element(By.XPATH,'//div[text()="OnePlus Nord CE 2 Lite 5G (Black Dusk, 128 GB)"]').click()
driver.find_element(By.XPATH,'//div[text()="OnePlus 11R 5G (Sonic Black, 256 GB)"]').click()
child_window=driver.window_handles
print(child_window)

for child in child_window:
    driver.switch_to.window(child)
driver.switch_to.window(parentwindow)
print("switched to parent window",parentwindow.title())