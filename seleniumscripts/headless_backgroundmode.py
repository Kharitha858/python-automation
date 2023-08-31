from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
opt=Options()
opt.headless=True
#or opt=add_argument('--headless')
#or opt=add_argument('--headless=new')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install(),chromeoptions=opt))
driver.get('https://www.flipkart.com/')
driver.maximize_window()
driver.get_screenshot_as_file('screenshot.png')