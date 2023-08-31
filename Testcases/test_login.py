import pytest
from selenium import webdriver
from Pageobjects.Login_page import Login
from Pageobjects.Homepage import Homepage
from Pageobjects.Homedesignation import Homedesignation
class Test_Login:
    baseURL='http://10.10.20.23:3001/'
    click_loginsignup_xpath = '//p[text()="Login/SignUp"]'
    click_loginasadmin_xpath = '//p[text()="Login/SignUp"]'
    username='Raunak'
    password='1234'


    def test_login(self,setup):
        self.driver=setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.clickloginsignup()
        self.lp.clickloginasadmin()
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        print("welcome to GOS")
        self.hp=Homepage(self.driver)
        # self.hp.mover_dashboard()
        self.hp.click_homepage()
        # self.hp.click_companyprofile()
        # self.hp.click_registration()
        # self.hp.click_mybookings()
        # self.hp.click_invoice()
        # self.hp.click_inhouseaccounts()
        # self.hp.click_calender()
        # self.hp.click_reports()

        #home
        self.hp.clkbasic()
        # self.hp.clklocation()
        # self.hp.clkhotel()
        # self.hp.clkagent()
        # self.hp.clkpackage()
        # self.hp.clkpaymentgateway()
        # self.hp.clkcommunicationmail()
        # self.hp.clkhouseboat()
        # self.hp.clkcoupon()

        #Basic settings:
        self.hp.clkdesignation()
        self.desg=Homedesignation(self.driver)
        # self.desg.clkback()
        # self.desg.clksearchbar()
        self.desg.tabledata()
        self.desg.clkcreatebtn()
        self.desg.designation()
        self.desg.clkresetbtn()
        self.desg.designation()
