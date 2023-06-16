from selenium.webdriver.common.by import By
from Source.Base.base_page import BasePage
from selenium import webdriver

class LoginPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.usernameFieldLocator = (By.XPATH, "//input[@name='email']")
        self.signinFieldLocator = (By.CLASS_NAME, 'a-button-input')
        self.passwordFieldLocator = (By.XPATH, "//input[@id='ap_password']")
        self.submitFieldLocator = (By.XPATH, "//input[@id='signInSubmit']")

    def fill_username_field(self, username):
        usernameFieldElement = self.find_element(self.usernameFieldLocator)
        self.send_keys(usernameFieldElement, username)

    def press_to_signin_button(self):
        signinButtonElement = self.find_element(self.signinFieldLocator)
        self.click(signinButtonElement)

    def fill_password_field(self, password):
        passwordFieldElement = self.find_element(self.passwordFieldLocator)
        self.send_keys(passwordFieldElement, password)

    def submit_button(self):
        submitButtonElement = self.find_element(self.submitFieldLocator)
        self.click(submitButtonElement)



