import pytest
import time

from selenium_programs.webdriver.chrome.options import Options

from pageObjects.Login_page import Login
from pageObjects.Demographics_page import Demographics
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-setuid-sandbox')
# chrome_options.add_argument('--remote-debugging-port=9222')
# chrome_options.add_argument('--disable-extensions')
# chrome_options.add_argument('start-maximized')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

import string
import random

class Test_003_demographics:
    baseURl = Readconfig.getApplicationURL()
    username = Readconfig.getusername()
    password = Readconfig.getuserpassword()

    logger = LogGen.loggen()  #Logger

    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_demographics(self,setup):
        self.logger.info("******Test_003_demographics**************")
        self.driver=setup
        self.driver.get(self.baseURl)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login successful*****")

        self.logger.info("******* Provoding client details***********")
        self.adddemo=Demographics(self.driver)

        # self.email=random_generator() + "gmail.com"
        # self.adddemo.setEmail(self.email)
        time.sleep(5)
        self.adddemo.setfullname("anitha")
        # time.sleep(5)
        # self.adddemo.setdateofbirth("23 jan 1997")
        time.sleep(5)
        self.adddemo.setgender("Male")
        time.sleep(5)
        self.adddemo.setaddress("ambur")
        time.sleep(5)
        self.adddemo.setpincode("635808")
        time.sleep(5)
        # self.adddemo.setcity("ambur")
        # time.sleep(5)
        # self.adddemo.setstate("Tamilnadu")
        # time.sleep(5)
        # self.adddemo.setcountry("India")
        # time.sleep(5)
        # self.adddemo.setnationality("INDIAN")
        self.adddemo.setmaritualstatus("Married")
        self.adddemo.setfamilytype("Joint Family")
        self.adddemo.seteducation("Master's Degree")
        self.adddemo.setoccupation("Engineer")
        self.adddemo.setdesignation("ASE")
        self.adddemo.setcompany("TYSS")
        self.adddemo.clickonnext()

        self.logger.info("************Saving client Info************")
        self.logger.info("*********Client details successfully adding****")
        self.toaster=self.driver.find_element('xpath','//div[@id="toast-container"]').text
        print(self.toaster)
        if 'Clients Deatils Updated Successfully' in self.toaster:
            assert True
            self.logger.info("******Demographics_page Test Passed*******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" +"Demographics.png")
            self.logger.error("******demographics Test failed***********")
            assert False

        self.driver.close()
        self.logger.info("*********Ending Demographics Test Failed*******")

    # def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    #     return "".join(random.choice(chars) for i in range(size))