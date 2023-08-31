import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.action_chains import ActionChains
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://www.flipkart.com/")
# driver.find_element(By.XPATH,'//button[text()="✕"]').click()
# element=driver.find_element(By.XPATH,'//div[@class="_3sdu8W emupdz"]//span[@class="_1XjE3T"]//span[text()="Home & Furniture"]//ancestor::div[@class="YBLJE4"]')
# act=ActionChains(driver)
# act.move_to_element(element).perform()
n = int(input("please give a number for fibonacci series : "))
first, second = 0, 1


def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


print("fibonacci series are : ")
for i in range(0, n):
    print(fibonacci(i))
