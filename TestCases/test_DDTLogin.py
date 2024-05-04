import time
import pytest
from PageObjects.LoginPage import Loginpg
from utilities.readProperties import ReadConfig
from utilities.customLogger import LoggenClass
from utilities import XLUtils


class Test_002DDT_Login:
    path=".//TestData/Test_Data.xlsx"
    log=LoggenClass.log_generator()

    @pytest.mark.regression
    def test_LoginDDT(self, setup):

        self.log.info("****** Login Page DDT testCase started *******")
        self.driver = setup
        self.lp = Loginpg(self.driver)
        self.rowno=XLUtils.getRowCount(self.path,'Sheet1')
        print("No of rows in excel file :", self.rowno)

        lst_status=[]   ##This is empty list variable

        for r in range(2,self.rowno+1):
            self.user=XLUtils.ReadData(self.path,'Sheet1',r,2)
            self.passw=XLUtils.ReadData(self.path,'Sheet1',r,3)

            print(self.user)
            print(self.passw)
            self.exp=XLUtils.ReadData(self.path,'Sheet1',r,4)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.passw)
            self.lp.clickLogin()
            time.sleep(2)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:  # PASS CONDITION
                if self.exp=="Pass":
                    self.log.info("******DDT Test Passed**********")
                    self.driver.back()
                    lst_status.append('Pass')
                elif self.exp=="Fail":
                    self.log.info("******DDT Test Failed**********")
                    # self.driver.back()
                    lst_status.append('Fail')
            elif act_title!=exp_title:  # FAIL CONDITION
                if self.exp=='Pass':
                    self.log.info("******DDT Test Failed**********")
                    # self.driver.back()
                    lst_status.append('Fail')
                elif self.exp=='Fail':
                    self.log.info("******DDT Test Passed**********")
                    # self.driver.back()
                    lst_status.append('Pass')

        if "Fail" not in lst_status:
            self.log.info("Login DDT test Passed")
            self.driver.close()
            assert True
        else:
            self.log.info("Login DDT test Failed")
            self.driver.close()
            assert False

        self.log.info("***End of Login DDT test Case***")
        self.log.info("***End of Login DDT 002***")
