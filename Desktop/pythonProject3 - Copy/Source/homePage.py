from selenium.webdriver.common.by import By
from Source.Base.base_page import BasePage
from selenium import webdriver

class HomePage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.signInbuttonLocator = (By.ID, 'nav-link-accountList')

    def sign_in_press_button_locator(self):
        signInPressButtonElement = self.find_element(self.signInbuttonLocator)
        self.click(signInPressButtonElement)