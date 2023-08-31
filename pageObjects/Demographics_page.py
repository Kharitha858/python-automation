import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from program import driver


class Demographics:
    time.sleep(5)
    txt_fullname_xpath='//input[@formcontrolname="fullName"]'

    # txt_dateofbirth_xpath='(//span[@class="mat-button-wrapper"])[15]'
    # text_dob_xpath="//div[@class='mat-calendar-content']//tbody//tr//div[text()=' 1999 ']"
    # text_dom_xpath="//tbody[@class='mat-calendar-body']//div[text()=' JAN ']"
    btn_sex_male_xpath="//span[text()='Male']"
    btn_sex_female_xpath="//span[text()='Female']"
    txt_address_xpath='//input[@formcontrolname="address"]'
    txt_pincode_xpath='//input[@formcontrolname="pincode"]'
    txt_city_xpath='//input[@formcontrolname="city"]'
    txt_state_xpath='//input[@formcontrolname="state"]'
    txt_country_xpath='//input[@formcontrolname="country"]'
    # dpn_nationality_xpath='//mat-select[@formcontrolname="nationality"]'
    # dpn_nationality_indian_xpath='//span[text()="INDIAN"]'
    # dpn_nationality_nri_xpath='//span[text()="NRI"]'
    dpn_maritualstatus_xpath='//mat-select[@formcontrolname="maritalStatus"]'
    dpn_maritualstatus_unmarried_xpath='//span[text()="Unmarried"]'
    dpn_maritualstatus_married_xpath='//span[text()="Married"]'
    dpn_familytype_xpath='//mat-select[@formcontrolname="familyType"]'
    dpn_familytype_nuclear_xpath='//span[text()="Nuclear Family"]'
    dpn_familytype_joint_xpath='//span[text()="Joint Family"]'
    dpn_Education_xpath='//div[@id="mat-select-value-47"]'
    dpn_Education_mdegreexpath="//span[text()='Master's Degree']"
    dpn_occupation_xpath='//mat-select[@formcontrolname="occupation"]'
    dpn_occupation_engineer_xpath='//span[text()="Engineer"]'
    txt_designation_xpath='//input[@formcontrolname="designation"]'
    txt_company_xpath='//input[@formcontrolname="company"]'
    btn_next_xpath='//button[text()="Next"]'

    def __init__(self,driver):
        self.driver=driver

    # def setEmail(self,email):
    #     self.driver.find_element('xpath','//input[@formcontrolname="email"]').send_keys(email)
    # def setpassword(self,pwd):
    #     self.driver.find_element('xpath','//input[@name="password"]').send_keys(pwd)

    def setfullname(self,fullname):
        Fullname=self.driver.find_element('xpath',self.txt_fullname_xpath)
        Fullname.clear()
        Fullname.send_keys(fullname)

    # def setdateofbirth(self,dateofbirth):
    #     dob=self.driver.find_element('xpath',self.txt_dateofbirth_xpath)
    #     dob.click()
    #     # dob.clear()
    #     clickonyear=self.driver.find_element('xpath',self.text_dob_xpath)
    #     # # dob.send_keys(dateofbirth)
    #     clickonyear.click()
    #     clickonmonth=self.driver.find_element('xpath',self.text_dom_xpath)
    #     clickonmonth.click()
    def setgender(self,gender):
        if gender=='Male':
            m=self.driver.find_element('xpath',self.btn_sex_male_xpath)
        #     m.clear()
            m.click()
        #
        # elif gender=='Female':
        #     f=self.driver.find_element('xpath',self.btn_sex_female_xpath)
        #     f.clear()
        #     f.click()
        else:
            self.driver.find_element('xpath',self.btn_sex_female_xpath).click()

    def setaddress(self,address):
        add=self.driver.find_element('xpath',self.txt_address_xpath)
        add.clear()
        add.send_keys(address)

    def setpincode(self,pincode):
        pin=self.driver.find_element('xpath',self.txt_pincode_xpath)
        pin.clear()
        pin.send_keys(pincode)

    # def setcity(self,city):
    #     c=self.driver.find_element('xpath',self.txt_city_xpath)
    #     c.clear()
    #     c.send_keys(city)
    #
    # def setstate(self,state):
    #     self.driver.find_element('xpath',self.txt_state_xpath).send_keys(state)
    #
    # def setcountry(self,country):
    #     self.driver.find_element('xpath',self.txt_country_xpath).send_keys(country)

    # def setnationality(self,text):
    #     # nationality = ['INDIAN', 'NRI']
    #     # for nation in nationality:
    #         drp=Select(self.driver.find_element('xpath',self.driver.dpn_nationality_xpath))
    #         drp.select_by_visible_text(text)
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-select[@role='combobox' and @formcontrolname='nationality']"))).click()
    button = driver.find_element("xpath", "//span[text()='NRI']")
    time.sleep(6)
    driver.execute_script("arguments[0].click();", button)
    time.sleep(6)
    def setmaritualstatus(self,value):
            drp=Select(self.driver.find_element('xpath',self.dpn_maritualstatus_xpath))
            drp.select_by_visible_text(value)


    def setfamilytype(self,value):
        drp=Select(self.driver.find_element('xpath',self.dpn_familytype_xpath))
        drp.select_by_visible_text(value)

    def seteducation(self,value):
        drp=Select(self.driver.find_element('xpath',self.dpn_Education_xpath))
        drp.select_by_visible_text(value)

    def setoccupation(self,value):
        drp=Select(self.driver.find_element('xpath',self.dpn_occupation_xpath))
        drp.select_by_visible_text(value)

    def setdesignation(self,designation):
        self.driver.find_element('xpath',self.txt_designation_xpath).send_keys(designation)

    def setcompany(self,company):
        self.driver.find_element('xpath',self.txt_company_xpath).send_keys(company)

    def clickonnext(self):
        self.driver.find_element('xpath',self.btn_next_xpath).click()



