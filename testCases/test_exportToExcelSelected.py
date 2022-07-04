import time

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.ExportToExcelPage import ExportToExcel
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.XLUtilities import readData
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_006_ExportToExcelSelected():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassWord()
    logger = LogGen.loggen()
    file = "C:\\Users\\prade\\Downloads\\customers.xlsx"
    email= "victoria_victoria@nopCommerce.com"

    def test_exportToExcelSelected(self, setup):
        self.logger.info("*******Test_006_Export to Excel Selected ******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.setUserName(self.username)
        self.loginpage.setPassWord(self.password)
        self.loginpage.clickLogin()
        self.logger.info("****login Successfull****")
        self.logger.info("****starting ExportToExcelSelected Customers Test ***")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clcikOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.logger.info("*****starting Export option*****")
        exporttoexcelsel= ExportToExcel(self.driver)
        status = exporttoexcelsel.exportToExcelSelected(self.email)
        if status == True:
            assert True
        exporttoexcelsel.clcikOnExport()
        exporttoexcelsel.clickOnExportToExcelselected()
        time.sleep(1)
        self.logger.info("*****Verify file downloaded******")
        exporttoexcelsel.verifyDownloadedfile(self.file)
        self.logger.info("*****verify downloaded file data*******")
        exportEmail = readData(self.file,"Customer",2,3)
        if exportEmail == self.email:
            assert True
            self.logger.info("***data Matches***")
        exporttoexcelsel.removeDownloadedfile(self.file)
        self.logger.info("***File deleted from folder***")
        self.logger.info("***TC_ExporToExcelSelected_006 is Finished***")
        self.driver.close()



