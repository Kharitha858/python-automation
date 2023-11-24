from selenium_programs import webdriver
from selenium_programs.webdriver.chrome.options import Options
opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")
driver=webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=opt)
driver.get("https://flipkart.com")