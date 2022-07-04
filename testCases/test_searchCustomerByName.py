import time

import pytest

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_0045_SearchCustomerByName():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassWord()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("*******Test_005_SearchCustomerByName******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.setUserName(self.username)
        self.loginpage.setPassWord(self.password)
        self.loginpage.clickLogin()
        self.logger.info("****login Successfull****")
        self.logger.info("****starting Search Customer By Name Test ***")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clcikOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.logger.info("****starting search customer by Name")
        seacrhcust = SearchCustomer(self.driver)
        seacrhcust.setFirstName("Victoria")
        seacrhcust.setLastName("Terces")
        seacrhcust.clickOnSearch()
        time.sleep(3)
        status = seacrhcust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("***TC_SearchCustomerByName_005 is Finished***")
        self.driver.close()

