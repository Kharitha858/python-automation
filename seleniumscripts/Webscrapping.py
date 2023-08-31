import time

from openpyxl.workbook import Workbook
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException
import smtplib
from email.message import EmailMessage
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.flipkart.com/')
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.XPATH,'//button[text()="✕"]').click()
driver.find_element(By.XPATH,'//div[@class="col-12-12 _2oO9oE"]').click()
driver.find_element(By.XPATH,'//input[@title="Search for products, brands and more"]').send_keys('Oneplus mobiles')
driver.find_element(By.XPATH,'//button[@class="L0Z3Pu"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//div[text()="OnePlus"]').click()
oneplusmobiles=driver.find_elements(By.XPATH,'//div[contains(@class,"_1YokD2 _3Mn1Gg")]//div[contains(text(),"OnePlus ")]')
mobileprices=driver.find_elements(By.XPATH,'//div[@class="_25b18c"]')
m=[]
p=[]
for mobile in oneplusmobiles:
    try:
        # print(mobile.text)
        m.append(mobile.text)

        # if 'OnePlus Nord 2T 5G (Gray Shadow, 128 GB)' in mobile.text:
        #     driver.execute_script("window.scrollTo(0, 1000);")
        #     time.sleep(4)
        #     mobile.click()
    except StaleElementReferenceException as Exception:
        # print('StaleElementReferenceException while trying to find mobiles')
        driver.execute_script("window.scrollTo(0, 1000);")
        # mobile.click()
        pass

for price in mobileprices:
    try:
        # print(price.text)
        p.append(price.text)
    except StaleElementReferenceException as Exception:
        # print('StaleElementReferenceException while trying to find mobile price')
        driver.execute_script("window.scrollTo(0, 1000);")
        pass
# print("mobile name:",m ,end="")
# # print('@'*10)
# print("Mobile price:", p, end="")
finallymp=zip(m,p)
# for data in list(finallymp):
    # print(data)
wb=Workbook()
wb["Sheet"].title='Oneplus mobiles'
sh1=wb.active
sh1.append(['Name','Price'])
for i in list(finallymp):
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 1000);")
    sh1.append(i)

wb.save("Finalrecordsnew1.xlsx")

#@@@@@@@@@@@@@@@@Sending email with attachement:
msg=EmailMessage()
msg['subject']='data'
msg['From']='Automation'
msg['To']='kharitha1304@gmail.com'
with open('EmailTemplate.txt') as myfile:
    data=myfile.read()
    msg.set_content(data)

with open('Finalrecordsnew1.xlsx','rb') as f:
    file_data=f.read()
    print('file data in binary',file_data)
    file_name=f.read()
    print('file name is',file_name)
    msg.add_attachment(file_data,maintype='application',subtype='xlsx',filename='file_name')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
    server.login('kharitha858@gmail.com','Hari&ganesh777')
    server.send_message(msg)

print('Email Sent!...')





















