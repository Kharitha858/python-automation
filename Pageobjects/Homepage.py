import self as self
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Homepage:
    #sidebar paths:
    mover_dashboard_xpath = '//div[@class="ant-layout-sider-children"]//descendant::p[text()="Dashboard"]//ancestor::li'
    mover_homeicon_xpath = '//div[@class="ant-layout-sider-children"]//descendant::p[text()="Manage Master"]//ancestor::li'
    mover_companyprofile_xpath='//div[@class="ant-layout-sider-children"]//descendant::p[text()="Company Profile"]//ancestor::li'
    mover_registration_xpath='//div[@class="ant-layout-sider-children"]//descendant::p[text()="Registration"]//ancestor::li'
    mover_mybookings_xpath='//div[@class="ant-layout-sider-children"]//descendant::p[text()="My Booking"]//ancestor::li'
    mover_invoice_xpath='//div[@class="ant-layout-sider-children"]//descendant::p[text()="Invoice"]//ancestor::li'
    mover_inhouseaccounts_xpath='//div[@class="ant-layout-sider-children"]//descendant::p[text()="Inhouse Accounts"]//ancestor::li'
    mover_calender_xpath='//div[@class="ant-layout-sider-children"]//descendant::p[text()="Calendar"]//ancestor::li'
    # mover_extranetcontentrate_xpath='//div[@class="ant-layout-sider-children"]//descendant::p[text()="Extranet Contract Rate"]//ancestor::li'
    mover_reports_xpath='//div[@class="ant-layout-sider-children"]//descendant::p[text()="Report"]//ancestor::li'

    # Home menu paths:
    clk_basicsettings_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="  Basic Settings"]'
    clk_locationsettings_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()=" Location Settings"]'
    clk_hotelsettings_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="  Hotel Settings"]'
    clk_agentsettings_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="  Agent Settings"]'
    clk_packagesettings_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="  Package Settings"]'
    clk_paymentgateway_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Payment Gateway"]'
    clk_communicationmail_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Communication Mail"]'
    clk_houseboatsettings_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="HouseboatSettings"]'
    clk_coupon_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Coupon"]'

    #Basic settings menu Xpath:
    clk_designation_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Designation"]'
    clk_bank_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Bank"]'
    clk_currency_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Currency"]'
    clk_assignmenu_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Assign Menu"]'
    clk_contacttype_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Contact Type"]'
    clk_markuptype_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Markup Type"]'

    #Location settings menu Xpath:
    clk_markettype_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Market Type"]'
    clk_region_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Region"]'
    clk_country_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Country"]'
    clk_province_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Province"]'
    clk_destination_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Destination"]'

    #Hotel settings menu xpath:
    clk_hotelcategory_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Hotel Category"]'
    clk_hoteltype_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Hotel Type"]'
    clk_occupancytype_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Occupancy Type"]'
    clk_seasontype_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Season Type"]'
    clk_roomcategory_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Room Category"]'
    clk_roomtype_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Room Type"]'
    clk_hotelamenity_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Hotel Amenity"]'
    clk_roomamenity_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Room Amenity"]'
    clk_mealplan_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Meal Plan"]'

    #agent settings menu xpath:
    clk_agentcattegory_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Agent Category"]'

    #package settings menu xpath:
    clk_packagecategory_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Package Category"]'
    clk_packagetype_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Package Type"]'
    clk_dayactivities_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Day Activities"]'
    clk_itinerarydetails_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Itinerary Details"]'
    clk_visainformation_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Visa Information"]'
    clk_termsandconditions_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Terms and Conditions"]'

    #houseboat settings menu xpath:
    clk_houseboattype_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="HouseboatType"]'
    clk_houseboatroomcategorytype_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Houseboatroomcategory"]'
    clk_houseboatroomtype_xpath='//ul[@class="ant-menu ant-menu-sub ant-menu-vertical"]//p[text()="Houseboatroomtype"]'


    def __init__(self,driver):
        self.driver = driver
        self.driver.actions=ActionChains(self.driver)
        self.driver.wait=WebDriverWait(self.driver, 30)

# Sidebarmenus:

    def  mover_dashboard(self):
        # self.driver.a= ActionChains(self.driver)
        # self.driver.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.mover_dashboard_xpath)))

        self.driver.actions.move_to_element(self.mover_dashboard_xpath).perform()
    def click_homepage(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.mover_homeicon_xpath))).click()
        # homeicon=self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.mover_homeicon_xpath)))
        # self.driver.actions.move_to_element(homeicon).perform()

    def click_companyprofile(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.mover_companyprofile_xpath))).click()

    def click_registration(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.mover_registration_xpath))).click()

    def click_mybookings(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.mover_mybookings_xpath))).click()

    def click_invoice(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.mover_invoice_xpath))).click()

    def click_inhouseaccounts(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.mover_inhouseaccounts_xpath))).click()

    def click_calender(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.mover_calender_xpath))).click()

    def click_reports(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.mover_reports_xpath))).click()


# Home Icon menu methods:

    def clkbasic(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_basicsettings_xpath))).click()

    def clklocation(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_locationsettings_xpath))).click()

    def clkhotel(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_hotelsettings_xpath))).click()

    def clkagent(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_agentsettings_xpath))).click()

    def clkpackage(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_packagesettings_xpath))).click()

    def clkpaymentgateway(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_paymentgateway_xpath))).click()
        # self.driver.navigate.get('http://10.10.20.23:3001/admin/dashboard')

    def clkcommunicationmail(self):
        self.driver.wait.until(EC.invisibility_of_element((By.XPATH,self.clk_communicationmail_xpath)))
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_communicationmail_xpath))).click()

    def clkhouseboat(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_houseboatsettings_xpath))).click()

    def clkcoupon(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_coupon_xpath))).click()

#Basic settings menu methods:

    def clkdesignation(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_designation_xpath))).click()

    def clkbank(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_bank_xpath))).click()

    def clkcurrency(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_currency_xpath))).click()

    def clkassignmenu(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_assignmenu_xpath))).click()

    def clkcontacttype(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_contacttype_xpath))).click()

    def clkmarkuptype(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_markuptype_xpath))).click()









