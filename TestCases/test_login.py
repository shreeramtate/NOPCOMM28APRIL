import pytest
from PageObjects.LoginPage import Loginpg
from utilities.readProperties import ReadConfig
from utilities.customLogger import LoggenClass


class Test_001_Login:

    useremail = ReadConfig.getUsername()
    Password = ReadConfig.getPassword()

    log=LoggenClass.log_generator()

    @pytest.mark.regression
    def test_HomePage(self, setup):
        self.log.info("****** Test_001*******")
        self.log.info("******Verfifying home page title*******")

        self.driver = setup
        act_title=self.driver.title

        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.log.info("****** Home Page testCase passed*******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\Homepg.png")
            self.driver.close()
            self.log.error("****** Home Page testCase failed*******")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):
        self.log.info("****** Login Page testCase started*******")
        self.driver = setup
        self.lp = Loginpg(self.driver)
        self.lp.setUsername(self.useremail)
        self.lp.setPassword(self.Password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.log.info("****** Login Page testCase Passed*******")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\LoginPage.png")
            self.log.error("****** Login Page testCase Failed*******")

            self.driver.close()
            assert False

#pytest -v -s TestCases/test_login.py --browser edge
#pytest -v -s -n=2 TestCases/test_login.py --browser fireforx

#pytest -v -s -m "sanity"--html=./Reports/Report1.html TestCases/ --browser edge
