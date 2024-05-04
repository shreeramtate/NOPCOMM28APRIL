import pytest
import time
import string
import random

from selenium.webdriver.common.by import By

from PageObjects.AddCustomer import AddCust
from PageObjects.LoginPage import Loginpg
from utilities.customLogger import LoggenClass
from utilities.readProperties import ReadConfig
from PageObjects.SearchCust import SearchCustomer

class Test_SearchCustomerByEmail:

    useremail = ReadConfig.getUsername()
    Password = ReadConfig.getPassword()

    log=LoggenClass.log_generator()

    # @pytest.mark.regression
    def test_SearchCustByEmail(self,setup):
        self.log.info("****** Search Customer by Email******")
        self.driver = setup
        self.lp = Loginpg(self.driver)
        self.ac = AddCust(self.driver)
        self.sc = SearchCustomer(self.driver)

        self.lp.setUsername(self.useremail)
        self.lp.setPassword(self.Password)
        self.lp.clickLogin()
        self.ac.ClickOnCustomers_Menu()
        self.ac.ClickOnCustomers_Sub_menu()

        self.sc.set_Email('james_pan@nopCommerce.com')
        self.sc.click_Search()
        self.sc.SearchCustBy_email('james_pan@nopCommerce.com')

        # if status==True:
        #     self.log.info("****** Search Customer Test Passed ******")
        #     print("Test Case Passed")
        #     assert True
        # else:
        #     self.log.info("****** Search Customer Failed ******")
        #     print("Test Case Failed")
        #     assert False
        # time.sleep(2)
        #
        # self.log.info("****** Search Customer By email Test case Finished******")
        # self.driver.close()


