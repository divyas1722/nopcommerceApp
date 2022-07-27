import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_login():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassWord()
    logger = LogGen.loggen()

    @pytest.fixture()
    def log_on_failure(request, get_browser):
        yield
        item = request.node
        driver = get_browser
        if item.rep_call.failed:
            allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        #self.logger.info("************Test_001_login********* ")
        self.logger.info("************verify home page Title********* ")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title ==  "Your store. Logi":
            assert True
            self.driver.close()
            self.logger.info("*******Home page Ttitle test is passed******")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("*******Home page Ttitle test is Failed******")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*******Verifying the login test******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.setUserName(self.username)
        self.loginpage.setPassWord(self.password)
        self.loginpage.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*******login test is passed******")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("*******login test is Failed******")
            assert False




