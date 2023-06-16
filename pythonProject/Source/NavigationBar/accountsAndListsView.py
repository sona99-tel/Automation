from selenium.webdriver.common.by import By
from Source.Base.base_page import BasePage

class ActionsAndViewsWindow(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.accountsAndViewsButtonLocator = (By.ID, "nav-link-accountList-nav-line-1")
        self.displayedAccountsAndViewsWindowHeadingLocator = (By.XPATH, "//div[@id='nav-al-title']")
        self.accountButtonLocator = (By.LINK_TEXT, "Account")
        self.accountPageTitleLocator = (By.XPATH, "//div[@id='nav-al-your-account'][1]")

    def move_on_accounts_and_lists_button(self):
        actionsAndViewsButtonElement = self.find_element(self.accountsAndViewsButtonLocator)
        self.mouse_move(actionsAndViewsButtonElement)

    def heading_of_displayed_account_and_lists_window(self):
        displayedAccountAndListsWindowElement = self.find_element(self.displayedAccountsAndViewsWindowHeadingLocator)
        message = displayedAccountAndListsWindowElement.text
        return message

    def click_on_accounts_button(self):
        accountButtonElement = self.find_element(self.accountButtonLocator)
        self.click(accountButtonElement)

    def title_of_the_opened_account_page(self):
        accountButtonElement = self.find_element(self.accountPageTitleLocator)
        message = accountButtonElement.text
        return message