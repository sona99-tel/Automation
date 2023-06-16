from selenium.webdriver.common.by import By
from Source.Base.base_page import BasePage

class YourOrdersPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.cancelledOrderButtonLocator = (By.XPATH, "//li[@class='page-tabs__tab'][5]")
        self.cancelledOrderPageDisplayedMessageLocator = (By.CLASS_NAME, "a-section a-spacing-top-medium a-text-center")

    def click_cancelled_orders_button(self):
        cancelledOrderButtonElement = self.find_element(self.cancelledOrderButtonLocator)
        self.click(cancelledOrderButtonElement)

    def get_message_in_cancelled_orders_page(self):
        cancelledOrderPageDisplayedMessageElement = self.find_element(self.cancelledOrderPageDisplayedMessageLocator)
        message = cancelledOrderPageDisplayedMessageElement.text
        return message