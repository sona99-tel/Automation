from selenium.webdriver.common.by import By
from Source.Base.base_page import BasePage

class SearchResultElementPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.clickFirstElementLocator = (By.XPATH, "//div[@class='aok-relative']/span[1]")

    def click_on_first_element(self):
        firstClickedElementLocator = self.find_element(self.clickFirstElementLocator)
        self.click(firstClickedElementLocator)




