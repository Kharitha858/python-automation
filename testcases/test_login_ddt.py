import time

import pytest
from selenium_programs import webdriver
from pageObjects.Login_page import Login
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen
from Utilities import XLutilis
import time

class Test_02_DDT_Login:
    baseURl = Readconfig.getApplicationURL()
    path= ".//TestData/medifit_datadriven.xlsx"

    logger = LogGen.loggen()

    def test_login_ddt(self,setup):
        self.logger.info("**************Test_02_DDT_Login***************")
        self.logger.info('************Verifying Login ddt page*********')
        self.driver=setup
        self.driver.get(self.baseURl)
        self.driver.maximize_window()

        self.lp=Login(self.driver)

        self.rows=XLutilis.getRowCount(self.path,'Sheet1')
        print("no of rows in excel:",self.rows)
        lst_status=[]  #empty list variable
        for r in range(2,self.rows+1):
            self.user=XLutilis.readData(self.path,'Sheet1',r,1)
            self.pwd = XLutilis.readData(self.path, 'Sheet1', r, 2)
            self.exp= XLutilis.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.pwd)
            self.lp.clickLogin()
            time.sleep(5)
            act_title=self.driver.title
            exp_title='MediFit'

            if act_title==exp_title:
                if self.exp=='Pass':
                    self.logger.info('*******Passed*******')
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp=='Fail':
                    self.logger.info('*******Failed*******')
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info('*******Failed*******')
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif self.exp == 'Fail':
                self.logger.info('*******Passed*******')
                self.lp.clickLogout()
                lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("Login ddt test passed...")
            self.driver.close()
            assert True
        else:

            self.logger.info("Login ddt test failed...")
            self.driver.close()
            assert False
        self.logger.info("*******End of Login DDT Test********...")
        self.logger.info("***********Completed Test_02_DDT_Login**********")


