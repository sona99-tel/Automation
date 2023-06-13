from Source.Base.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductDetails(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.addInCartButtonLocator = (By.XPATH, "//input[@id='add-to-cart-button']")

    def adding_cart_button_locator(self):
        addingCartButtonElement = self.find_element(self.addInCartButtonLocator)
        self.click(addingCartButtonElement)