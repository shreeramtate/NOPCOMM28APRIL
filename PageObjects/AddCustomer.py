from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select


class AddCust:
    Customers_Menu_XPath="//a[@href='#']//p[contains(text(),'Customers')]"
    Customers_SubMenu_Xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    Add_NewCust_XPath="//a[normalize-space()='Add new']"
    txtEnter_EmailidCSS="#Email"
    txtEnter_PasswordCSS="#Password"
    txtFirst_NameCSS="#FirstName"
    txtLast_NameCSS="#LastName"
    RdGender_Male_xpath="//input[@id='Gender_Male']"
    RdGender_Female_xpath="//input[@id='Gender_Female']"
    txtDOB_input_XPath="//input[@id='DateOfBirth']"
    txtCompany_input_XPath="//input[@id='Company']"
    lstNewsLetter_XPath="//input[@aria-expanded='true']"
    lstCustRoles_clear_xpath="//span[@title='delete']"
    lstCustomer_role_Listbox_Xpath="//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstCustomer_role_Regi_Xpath="//span[normalize-space()='Registered']"
    lstCustomer_Role_guest_XPath="//li[@id='63201d9f-3d51-4875-a568-929f785475b3']"
    lstManager_Vendor_XPath="//select[@id='VendorId']"
    checkbox_Active_XPath="//*[@id='Active']"
    lstManager_Comment_XPath="//textarea[@id='AdminComment']"
    btnSave_XPath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def ClickOnCustomers_Menu(self):
        self.driver.find_element(By.XPATH,self.Customers_Menu_XPath).click()

    def ClickOnCustomers_Sub_menu(self):
        self.driver.find_element(By.XPATH, self.Customers_SubMenu_Xpath).click()

    def ClickAddNew_Customers(self):
        self.driver.find_element(By.XPATH, self.Add_NewCust_XPath).click()

    def SetEmail(self,email):
        self.driver.find_element(By.CSS_SELECTOR, self.txtEnter_EmailidCSS).send_keys(email)

    def SetPassword(self,password):
        self.driver.find_element(By.CSS_SELECTOR, self.txtEnter_PasswordCSS).send_keys(password)

    def SetFirst_Name(self,Fname):
        self.driver.find_element(By.CSS_SELECTOR, self.txtFirst_NameCSS).send_keys(Fname)

    def SetLast_Name(self,Lname):
        self.driver.find_element(By.CSS_SELECTOR, self.txtLast_NameCSS).send_keys(Lname)

    def SetDOB(self,dob):
        self.driver.find_element(By.XPATH, self.txtDOB_input_XPath).send_keys(dob)

    def SetCompany_name(self,company):
        self.driver.find_element(By.XPATH, self.txtCompany_input_XPath).send_keys(company)


    def SetCustomer_Role(self,role):
        self.driver.find_element(By.XPATH,self.lstCustRoles_clear_xpath).click()
        self.listItem=Select(self.driver.find_element(By.XPATH,self.lstCustomer_role_Listbox_Xpath).click())
        if role=='Registered':
            self.listItem.select_by_visible_text(role)
        elif role=='Guests':
            self.listItem.select_by_visible_text(role)
        elif role == 'Vendors':
            self.listItem.select_by_visible_text(role)
        else:
            self.listItem.select_by_visible_text('Guests')

    def SetManager_vendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.lstManager_Vendor_XPath))
        drp.select_by_visible_text(value)

    def SetGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.XPATH,self.RdGender_Male_xpath).click()
        elif gender=='Female':
            self.driver.find_element(By.XPATH,self.RdGender_Female_xpath).click()

    def Add_Comment(self,comment):
        self.driver.find_element(By.XPATH, self.lstManager_Comment_XPath).send_keys(comment)

    def ClickOn_Save(self): #btnSave_XPath
        self.driver.find_element(By.XPATH, self.btnSave_XPath).click()












    #act_title= Customers / nopCommerce administration
    # save_msg="The new customer has been added successfully."