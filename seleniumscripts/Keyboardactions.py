import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://10.10.20.141:3000/")
driver.find_element(By.XPATH,'//p[text()="Login/SignUp"]').click()
driver.find_element(By.XPATH,'//span[text()=" Login as Admin"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//input[@type="username"]').send_keys("1234")
act=ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).send_keys(Keys.TAB).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).send_keys(Keys.ENTER).perform()