import time

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.ExportToExcelPage import ExportToExcel
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.XLUtilities import readData, getRowCount
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_008_ExportToExcelSelected_ddt():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassWord()
    logger = LogGen.loggen()
    file = "C:\\Users\\prade\\Downloads\\customers.xlsx"
    file_testdata= ".//TestData/loginDetails.xlsx"


    def test_exportToExcelSelected_ddt(self, setup):
        self.logger.info("*******Test_006_Export to Excel Selected_ddt ******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.setUserName(self.username)
        self.loginpage.setPassWord(self.password)
        self.loginpage.clickLogin()
        self.logger.info("****login Successfull****")
        self.logger.info("****starting ExportToExcelSelected_ddt Customers Test ***")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clcikOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.logger.info("*****starting Export option*****")
        self.rows = getRowCount(self.file_testdata, "customer")
        print("Number of rows in testdata file:", self.rows)
        exporttoexcelsel = ExportToExcel(self.driver)
        lst_checked = []
        for ro in range(2,self.rows+1):
            email = readData(self.file_testdata,'customer',ro,1)
            print(email)
            time.sleep(1)
            status = exporttoexcelsel.exportToExcelSelected(email)
            print("status:",status)
            if status == True:
                lst_checked.append("checked")
            else:
                lst_checked.append(("not checked"))
        print(lst_checked)
        if "not checked" not in lst_checked:
            self.logger.info("*** choosed checkboxes are selected***")
            assert True
        else:
            self.logger.info("****one or more checkboxes are not selected****")
            assert False
        exporttoexcelsel.clcikOnExport()
        exporttoexcelsel.clickOnExportToExcelselected()
        self.logger.info("*****Verify file downloaded******")
        exporttoexcelsel.verifyDownloadedfile(self.file)
        time.sleep(2)
        self.logger.info("*****verify downloaded file data*******")
        exportrows = getRowCount(self.file, "Customer")
        print("no of rows in output file:", exportrows)
        if exportrows == self.rows:
            assert True
            self.logger.info("***data Matches***")
        else:
            self.logger.info("***data doe not match in input and output files***")
            assert False
        time.sleep(3)
        exporttoexcelsel.removeDownloadedfile(self.file)
        self.logger.info("***File deleted from folder***")
        self.logger.info("***TC_ExporToExcelSelected_006 is Finished***")
        self.driver.close()



