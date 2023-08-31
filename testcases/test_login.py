import pytest
from selenium import webdriver
from pageObjects.Login_page import Login
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen


class Test_01_Login:
    baseURl = Readconfig.getApplicationURL()
    username = Readconfig.getusername()
    password = Readconfig.getuserpassword()

    logger = LogGen.loggen()

    def test_homepageTitle(self,setup):
        self.logger.info('************Test_01_Login*********')
        self.logger.info('************Verifying Home page title*********')
        self.driver=setup
        self.driver.get(self.baseURl)
        act_title=self.driver.title
        # self.driver.close()
        if act_title=="MediFit":
            assert True
            # self.driver.close()
            self.logger.info('************Home page tilte test is passed*********')
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            self.driver.close()
            self.logger.error('************Home page tilte test is failed*********')
            assert False

    def test_login(self,setup):
        self.logger.info('************Verifying Login page title*********')
        self.driver=setup
        self.driver.get(self.baseURl)
        self.driver.maximize_window()
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        # self.driver.close()
        if act_title=="MediFit":
            assert True
            self.logger.info('************Login page test is passed*********')
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error('************Login page test is failed*********')
            assert False
        self.lp=Login(self.driver)
        # self.lp.clickLogout()
    def test_LoginTitle(self):
        self.driver=webdriver.Chrome()
        self.driver.get(self.baseURl)
        act_title=self.driver.title
        # self.driver.close()
        if act_title=="MediFit":
            assert True
            self.logger.info('************Login page tilte test is passed*********')
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_LoginTitle.png")
            self.driver.close()
            self.logger.error('************Login page tilte test is passed*********')
            assert False


