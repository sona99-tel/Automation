from selenium.webdriver.common.by import By
from Source.Base.base_page import BasePage

class NavigationBar(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.searchingFieldLocator = (By.XPATH, "//input[@id='twotabsearchtextbox']")
        self.submitSearchLocator = (By.ID, "nav-search-submit-button")
        self.cartButtonLocator = (By.ID, "nav-cart-count-container")

    def fill_search_field(self, item):
        searchingFieldElement = self.find_element(self.searchingFieldLocator)
        self.send_keys(searchingFieldElement, item)

    def submit_search_button(self):
        submitSearchButtonElement = self.find_element(self.submitSearchLocator)
        self.click(submitSearchButtonElement)

    def click_to_cart_button(self):
        cartButtonElement = self.find_element(self.cartButtonLocator)
        self.click(cartButtonElement)
