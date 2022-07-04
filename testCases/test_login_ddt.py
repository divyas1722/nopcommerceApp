import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtilities


class Test_002_DDT__Login():
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/loginDetails.xlsx"
    #path = "C:\Users\prade\PycharmProjects1\nopcommerceApp\TestData\loginDetails.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("*******Verifying the login DDT test******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loginpage = LoginPage(self.driver)
        self.rows = XLUtilities.getRowCount(self.path,'Sheet2')
        print("Number of rows in excel:", self.rows)
        lst_status = []
        for r in range(2,self.rows+1):
            self.username = XLUtilities.readData(self.path,'Sheet2',r,1)
            self.password = XLUtilities.readData(self.path,'Sheet2',r,2)
            self.exp = XLUtilities.readData(self.path,'Sheet2',r,3)
            self.loginpage.setUserName(self.username)
            self.loginpage.setPassWord(self.password)
            self.loginpage.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("***passed***")
                    self.loginpage.clickLogOut()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***Failed***")
                    self.loginpage.clickLogOut()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("***Failed***")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("***passed***")
                    lst_status.append("pass")
        if "Fail" not in lst_status:
            self.logger.info("****login DDT passed***")
            self.driver.close()
            assert True
        else:
            self.logger.info("********login DDT failed***")
            self.driver.close()
            assert False

        self.logger.info("*******End of login DDT test****")
        self.logger.info("*****Completed test_002_login_DDT****")

