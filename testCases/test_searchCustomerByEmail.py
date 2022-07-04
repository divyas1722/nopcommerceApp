import time

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_SearchCustomerByEmail():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassWord()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("*******Test_004_SearchCustomerByEmail******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.setUserName(self.username)
        self.loginpage.setPassWord(self.password)
        self.loginpage.clickLogin()
        self.logger.info("****login Successfull****")
        self.logger.info("****starting Search Customer By Email Test ***")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clcikOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.logger.info("****starting search customer by EmailID")
        seacrhcust = SearchCustomer(self.driver)
        seacrhcust.setEmail("victoria_victoria@nopCommerce.com")
        seacrhcust.clickOnSearch()
        time.sleep(3)
        status = seacrhcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("***TC_SearchCustomerByEmail_004 is Finished***")
        self.driver.close()

