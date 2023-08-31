from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
class Homedesignation:

    clk_backbtn_xpath='//span[text()="Back"]'
    clk_searchbar_xpath='//div[@class="ant-col css-dev-only-do-not-override-ixblex"]//input[@placeholder="Search"]'
    txt_designation_xpath='//input[@name="designation"]'
    clk_createbtn_xpath='//div[text()="Create"]'
    popup_title_xpath='//label[@class="modal-title fw-600 ff-open-sans"]//p[text()="Create Designation"]'
    clk_windowcreate_xpath='//p[text()="Create"]'
    clk_validationmessage_xpath='//p[text()="Designation required"]'
    clk_resetbutton_xpath='//p[text()="Reset"]'
    # get_pagination_xpath='//li[contains(@class,"ant-pagination-item ant-pagination-item")]'
    # get_tabledata_xpath='//div[@class="ant-table-body"]//tr//td[2]'
    toastmeg_xpath='//div[text()="Designation Already Exists!"]'
    def __init__(self,driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 40)

    def clkback(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_backbtn_xpath))).click()

    def clksearchbar(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_searchbar_xpath))).click()

    def tabledata(self):
        pagenation = self.driver.find_elements(By.XPATH, '//li[contains(@class,"ant-pagination-item ant-pagination-item")]')
        for page in pagenation:
            page.click()
            time.sleep(2)
            data = self.driver.find_elements(By.XPATH, '//div[@class="ant-table-body"]//tr//td[2]')
            for desg in data:
                time.sleep(2)
                data = desg.text
                print(data)

    def clkcreatebtn(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_createbtn_xpath))).click()
        # title=self.driver.wait.until(EC.invisibility_of_element((By.XPATH, self.popup_title_xpath)))
        # title.is_displayed()
        # title.is_enabled()
        # print(title.text)
        #
        # # print(heading)
        # if title=="Create Designation":
        #     print(True)
        # else:
        #     print(False)

    # def designation(self):
    #     self.driver.wait.until(EC.element_to_be_clickable((By.XPATH,self.clk_windowcreate_xpath))).click()
    #     time.sleep(2)
    #     validationmessage=self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_validationmessage_xpath)))
    #     validationmessage.is_displayed()
    #     # print(validationmessage.text)
    #     if validationmessage=="Designation required":
    #         return True
    #     else:
    #         return False

    def designation(self):

        try:
            self.driver.set_page_load_timeout(1)
            self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_windowcreate_xpath))).click()
        except TimeoutException as ex:
            isrunning = 0
            print("Exception has been thrown. " + str(ex))

            # time.sleep(2)
        try:
            self.driver.set_page_load_timeout(1)
            validationmessage = self.driver.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.clk_validationmessage_xpath)))
            validationmessage.is_displayed()
            msg = validationmessage.text
            if msg == "Designation required":
                return True
            else:
                return False
        except TimeoutException as ex:
            print("Exception has been thrown. " + str(ex))

    def clkresetbtn(self):
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_resetbutton_xpath))).click()
        time.sleep(2)
        designation = self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.txt_designation_xpath))).send_keys("software engineer")
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self.clk_windowcreate_xpath))).click()
        t=self.driver.wait.until(EC.presence_of_element_located((By.XPATH,self.toastmeg_xpath)))
        print(t.text)
        # data = self.driver.find_elements(By.XPATH, '//div[@class="ant-table-body"]//tr//td[2]')
        # # for desg in data:
        # #     time.sleep(2)
        # #     print(desg.text)
        # if data == designation:
        #     print(self.driver.toastmeg_xpath.is_displayed())
