import pytest
import time
import string
import random

from selenium.webdriver.common.by import By

from PageObjects.AddCustomer import AddCust
from PageObjects.LoginPage import Loginpg
from utilities.customLogger import LoggenClass
from utilities.readProperties import ReadConfig


class Test_003_Addcustomer:

    useremail = ReadConfig.getUsername()
    Password = ReadConfig.getPassword()

    log=LoggenClass.log_generator()

    @pytest.mark.sanity
    def test_AddCustomer(self, setup):
        self.log.info("****** Add Customer TestCase started*******")
        self.driver = setup
        self.lp = Loginpg(self.driver)
        self.ac = AddCust(self.driver)
        self.lp.setUsername(self.useremail)
        self.lp.setPassword(self.Password)
        self.lp.clickLogin()
        self.log.info("********Logged in to main page*********")
        self.log.info("********Add customer steps started*********")
        self.ac.ClickOnCustomers_Menu()
        self.ac.ClickOnCustomers_Sub_menu()
        self.log.info("********Add new Customers Page started*********")
        self.ac.ClickAddNew_Customers()
        self.email=random_generator(8,string.ascii_lowercase+string.digits)+"@gmail.com"
        self.ac.SetEmail(self.email)
        self.ac.SetPassword('aayush123')
        self.ac.SetFirst_Name('Shree')
        self.ac.SetLast_Name('Tate')
        time.sleep(2)
        self.ac.SetGender("Male")
        self.ac.SetDOB('2/4/1985')
        self.ac.SetCompany_name("Franco")
        time.sleep(5)
        self.ac.SetManager_vendor("Vendor 1")
        time.sleep(3)
        # self.ac.SetCustomer_Role("Guests")

        self.ac.Add_Comment("This is for TESTING")
        self.ac.ClickOn_Save()
        self.log.info("********Saved Customer details*********")

        self.msg=self.driver.find_element(By.TAG_NAME,'body').text
        print(self.msg)

        if 'The new customer has been added successfully.' in self.msg:
            assert True
            self.log.info("*******Add Customer Test Case Passed Successfully**********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_AddCustomer.png")
            self.log.error("******Add cuustomer Test Case Failed**********")
            assert False

        self.driver.close()
        self.log.info("**********Ending Add customer TestCase *********")

def random_generator(size, chars):
    return ''.join(random.choice(chars) for x in range(size))