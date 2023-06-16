from selenium.webdriver.common.by import By
from Source.Base.base_page import BasePage

class CartPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.addInCartButtonLocator = (By.XPATH, "//input[@id='add-to-cart-button']")
        self.deleteButtonLocator = (By.XPATH, "//div[@class='a-row sc-action-links']/span[2]")
        self.deletedItemSuccessMessageLocator = (By.LINK_TEXT,  "Apple iPhone 14, 256GB, Midnight - Unlocked (Renewed Premium)")

    def click_to_delete_item(self):
        deleteButtonElement = self.find_element(self.deleteButtonLocator)
        self.click(deleteButtonElement)

    def get_success_message_of_deletion(self):
        deletedItemsuccessMessageLocator = self.find_element(self.deletedItemSuccessMessageLocator)
        message = deletedItemsuccessMessageLocator.text
        return message