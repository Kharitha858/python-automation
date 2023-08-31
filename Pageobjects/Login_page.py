from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Login:
    click_loginsignup_xpath='//p[text()="Login/SignUp"]'
    click_loginasadmin_xpath='//span[text()=" Login as Admin"]'
    txtbox_username_xpath='//input[@placeholder="Your Username*"]'
    txtbox_password_xpath='//input[@placeholder="Your Password"]'
    clickon_loginbtn_xpath="//button[text()=' Login']"

    def __init__(self,driver):
        self.driver=driver

    def clickloginsignup(self):
        self.driver.find_element(By.XPATH,self.click_loginsignup_xpath).click()

    def clickloginasadmin(self):
        # loginasadmin=self.driver.find_element(By.XPATH,self.click_loginasadmin_xpath)
        # loginasadmin.click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.click_loginasadmin_xpath))).click()

    def setusername(self,username):
        self.driver.find_element(By.XPATH,self.txtbox_username_xpath).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.XPATH,self.txtbox_password_xpath).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.clickon_loginbtn_xpath).click()

    