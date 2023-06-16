from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage():

    def __init__(self, driver: webdriver):
        self.driver = driver

    def find_element(self, locator):
        if self.is_element_visible(locator):
            element = self.driver.find_element(*locator)
            return element
        else:
            print("error")

    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def get_title(self):
        return self.driver.title()

    def clear_text(self, webElement):
        webElement.clear()

    def click(self, webElement):
        webElement.click()

    def send_keys(self, element, text):
        element.clear()
        element.send_keys(text)

    def mouse_move(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def get_text(self, webElement):
        webElement.text()