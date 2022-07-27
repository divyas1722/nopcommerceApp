import random
import string
import time

import allure
import pytest
from allure_commons.types import AttachmentType

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig



class Test_003_AddCustomer():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassWord()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("*******Test_003_AddCustomer******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.setUserName(self.username)
        self.loginpage.setPassWord(self.password)
        self.loginpage.clickLogin()
        self.logger.info("****login Successfull****")
        self.logger.info("****starting Add Customer Test ***")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clcikOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        time.sleep(1)
        self.addcust.clickOnAddnew()
        self.logger.info("****Providing Customer infor****")
        self.email = random_generator() + "@gmail.com"
        time.sleep(1)
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Viaan")
        self.addcust.setLastName("sakha")
        self.addcust.setGender("Male")
        self.addcust.setDOB("6/22/1990")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setAdminContent("This is for testing")
        self.addcust.clickOnSave()
        allure.attach(self.driver.get_screenshot_as_png(),name="addcustomer",attachment_type=AttachmentType.PNG)

        self.logger.info("****Add customer validation started****")
        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("***Add customer test passed ***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png")
            self.logger.info("***Add customer test Failed***")
            assert True ==False
        self.driver.close()
        self.logger.info("***Ending Add customer test****")

def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))

