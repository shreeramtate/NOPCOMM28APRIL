from selenium import webdriver
from selenium.webdriver.common.by import By


class Loginpg:
    textbox_username_ID="Email" #Email
    textbox_Password_ID="Password"  #Password
    button_Login_XPATH="//button[@type='submit']"   #
    button_Logout_Linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_ID).clear()
        self.driver.find_element(By.ID, self.textbox_username_ID).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_Password_ID).clear()
        self.driver.find_element(By.ID, self.textbox_Password_ID).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_Login_XPATH).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.button_Logout_Linktext).click()

