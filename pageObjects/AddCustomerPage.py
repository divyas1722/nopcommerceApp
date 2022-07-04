import time

from selenium.webdriver.support.select import Select


class AddCustomer:
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAdd_xpath ="//a[@class='btn btn-primary']"
    txtEmail_id="Email"
    txtPassword_id="Password"
    txtFirstName_id="FirstName"
    txtLastName_id="LastName"
    rdMaleGender_id="Gender_Male"
    rdFemaleGender_id="Gender_Female"
    txtDOB_id="DateOfBirth"
    txtCompanyName_id="Company"
    chbxTaxExempt_id="IsTaxExempt"
    txtCustomerRole_xpath="//ul[@id='SelectedCustomerRoleIds_taglist']"
    drpMgofVendor_id="VendorId"
    txtAdminContent_id="AdminComment"
    lstitemAdministrators_xpath="//li[text()='Administrators']"
    lstitemGuest_xpath="//li[text()='Guests']"
    lstitemRegistered_xpath="//li[text()='Registered']"
    lstitemVendor_xpath="//li[text()='Vendors']"
    lstitemForumModerator_xpath="//li[text()='Forum Moderators']"

    btnSave_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver= driver

    def clcikOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        menuitem = self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath)
        self.driver.execute_script('arguments[0].click()',menuitem)

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAdd_xpath).click()
    def setEmail(self,email):
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)
    def setPassword(self,password):
        self.driver.find_element_by_id(self.txtPassword_id).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(lastname)

    def setDOB(self,dob):
        self.driver.find_element_by_id(self.txtDOB_id).send_keys(dob)

    def setCompanyName(self,companyname):
        self.driver.find_element_by_id(self.txtCompanyName_id).send_keys(companyname)

    def setCustomerRoles(self,role):
        time.sleep(1)
        roles = self.driver.find_element_by_xpath(self.txtCustomerRole_xpath)
        self.driver.execute_script("arguments[0].click()", roles)
        time.sleep(3)

        if role =="Registered":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role =="Administrators":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role =="Guests":
            # Here user can be registered or guest, only one
            time.sleep(3)
            removelink = self.driver.find_element_by_xpath("//ul[@id='SelectedCustomerRoleIds_taglist']/li/span[2]/span")
            self.driver.execute_script("arguments[0].click()",removelink)
            time.sleep(1)
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuest_xpath)
        elif role =="Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendor_xpath)
        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemForumModerator_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuest_xpath)

        time.sleep(3)
        self.driver.execute_script("arguments[0].click()", self.listitem)
    def setManagerOfVendor(self,value):
        drp = Select(self.driver.find_element_by_id(self.drpMgofVendor_id))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setAdminContent(self,content):
        self.driver.find_element_by_id(self.txtAdminContent_id).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()



