from selenium.webdriver.common.by import By
from Source.Base.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.addInCartButtonLocator = (By.XPATH, "//input[@id='add-to-cart-button']")
        self.deleteButtonLocator = (By.NAME, "submit.delete.7eae8c91-74d7-424c-81d5-5b740b0a56e0")

    def deleting_item(self):
        deleteButtonElement = self.find_element(self.deleteButtonLocator)
        self.click(deleteButtonElement)
