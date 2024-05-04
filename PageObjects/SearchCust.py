from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchCustomer:

    txtSearch_Email_ID="SearchEmail"
    txtFirst_Name_Name="SearchFirstName"
    txtLast_Name_Name="SearchLastName"
    btnSearch_ID = "search-customers"
    table_xpath="//table[@id='customers-grid']"
    #//table[@id='customers-grid']
    tableRows_xpath="//*[@id='customers-grid']//tbody/tr"

    #//*[@id="customers-grid"]/tbody/tr/td[2]
    #//*[@id="customers-grid"]/tbody/tr/td[3]
    #//*[@id="customers-grid"]/tbody/tr/td[2]

    tableCol_xpath="//*[@id='customers-grid']//tbody//tr/td"

    def __init__(self, driver):
        self.driver = driver

    def set_Email(self,email):
        self.driver.find_element(By.ID,self.txtSearch_Email_ID).clear()
        self.driver.find_element(By.ID, self.txtSearch_Email_ID).send_keys(email)

    def set_FirstName(self,fname):
        self.driver.find_element(By.NAME,self.txtFirst_Name_Name).clear()
        self.driver.find_element(By.NAME,self.txtFirst_Name_Name).send_keys(fname)

    def set_LastName(self,lname):
        self.driver.find_element(By.NAME,self.txtLast_Name_Name).clear()
        self.driver.find_element(By.NAME,self.txtLast_Name_Name).send_keys(lname)

    def click_Search(self):
        self.driver.find_element(By.ID,self.btnSearch_ID).click()

    def get_Rows_Count(self):
        return len(self.driver.find_element(By.XPATH,self.tableRows_xpath))

    def get_Coloumns_Count(self):
        return len(self.driver.find_element(By.XPATH,self.tableCol_xpath))

    def SearchCustBy_email(self, email):
        flag=False
        emailid = self.driver.find_element(By.XPATH,"//*[@id='customers-grid']/tbody/tr/td[2]").text
        print(emailid)

        if email == emailid:
            flag=True
        else:
            flag =False
        return flag

    def SearchCustBy_Name(self,fname):
        flag=False
        tname=self.driver.find_element(By.XPATH,"//*[@id='customers-grid']/tbody/tr/td[3]").text
        if tname == fname:
            flag=True
        else:
            flag=True
        return flag
