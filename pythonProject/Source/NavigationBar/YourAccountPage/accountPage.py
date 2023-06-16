from selenium.webdriver.common.by import By
from Source.Base.base_page import BasePage

class YourAccountPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.yourProfileButtonLocator = (By.XPATH, "//img[@alt='Your Profiles']")
        self.profilePageTitleLocator = (By.ID, "home-heading")
        self.yourOrdersButtonLocator = (By.XPATH, "//div[@class='ya-card-cell'][1]")
        self.ordersPageTitleLocator = (By.TAG_NAME, "Your Orders")

    def click_your_profile_button(self):
        yourProfileButtonelement = self.find_element(self.yourProfileButtonLocator)
        self.click(yourProfileButtonelement)

    def title_of_profile_page(self):
        profilePageTitleElement = self.find_element(self.profilePageTitleLocator)
        message = profilePageTitleElement.text
        return message

    def click_your_orders_button(self):
        yourOrdersButtonelement = self.find_element(self.yourOrdersButtonLocator)
        self.click(yourOrdersButtonelement)

    def title_of_orders_page(self):
        ordersPageTitleElement = self.find_element(self.ordersPageTitleLocator)
        title = ordersPageTitleElement.text
        return title
