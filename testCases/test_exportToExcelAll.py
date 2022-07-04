import time

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.ExportToExcelPage import ExportToExcel
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.XLUtilities import readData, getRowCount
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_006_ExportToExcelSelected():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassWord()
    logger = LogGen.loggen()
    file = "C:\\Users\\prade\\Downloads\\customers.xlsx"

    def test_exportToExcelAll(self, setup):
        self.logger.info("*******Test_007_Export to Excel All ******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.setUserName(self.username)
        self.loginpage.setPassWord(self.password)
        self.loginpage.clickLogin()
        self.logger.info("****login Successfull****")
        self.logger.info("****starting ExportToExcelAll Customers Test ***")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clcikOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.logger.info("*****starting Export option*****")
        exporttoexcelall = ExportToExcel(self.driver)
        rowCount = exporttoexcelall.getNoOfRows()
        exporttoexcelall.clcikOnExport()
        exporttoexcelall.clickOnExportToExcelAll()
        self.logger.info("*****Verify file downloaded******")
        exporttoexcelall.verifyDownloadedfile(self.file)
        self.logger.info("*****verify downloaded file data*******")
        time.sleep(2)
        exportrows = getRowCount(self.file,"Customer")
        if exportrows == rowCount:
            assert True
            self.logger.info("***data Matches***")
        exporttoexcelall.removeDownloadedfile(self.file)
        self.logger.info("***File deleted from folder***")
        self.logger.info("***TC_ExporToExcelAll_007 is Finished***")
        self.driver.close()



