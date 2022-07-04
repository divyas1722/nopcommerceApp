import time

from pageObjects.SearchCustomerPage import SearchCustomer
import openpyxl
import os.path

from utilities.XLUtilities import readData


class ExportToExcel(SearchCustomer):
    btnExport_xpath = "//button[@class='btn btn-success']/i"
    lnkExportToExcelAll_xpath="//button[@name='exportexcel-all']"
    lnkExportToExcelSelected_xpath = "//button[@id='exportexcel-selected']"

    def exportToExcelSelected(self, email):
        time.sleep(2)
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            print(r)
            time.sleep(2)
            table = self.driver.find_element_by_xpath(self.table_xpath)
            print(table)
            self.driver.execute_script("return arguments[0].scrollIntoView(true);", table)
            row = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr[" + str(r) + "]")
            print(row)
            emailid = row.find_element_by_xpath("td[2]").text
            if emailid == email:
                time.sleep(1)
                row.find_element_by_xpath("td[1]").click()
                flag = True
        return flag


    def clcikOnExport(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.btnExport_xpath).click()

    def clickOnExportToExcelselected(self):
        time.sleep(2)
        exportToExcel = self.driver.find_element_by_xpath(self.lnkExportToExcelSelected_xpath)
        self.driver.execute_script('arguments[0].click()', exportToExcel)

    def clickOnExportToExcelAll(self):
        exportAll = self.driver.find_element_by_xpath(self.lnkExportToExcelAll_xpath)
        self.driver.execute_script('arguments[0].click()', exportAll)

    def verifyDownloadedfile(self,file):
        if os.path.exists(file):
            return True
    def removeDownloadedfile(self,file):
        os.remove(file)
        return True





