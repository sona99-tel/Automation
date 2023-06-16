from Source.loginPage import LoginPage
from Source.NavigationBar.accountsAndListsView import ActionsAndViewsWindow
from Source.homePage import HomePage
from Tests.base_test.base_test import BaseTest
import time

class TestCase(BaseTest):

    def test_accounts_and_view_window(self):
        self.driver.get("https://www.amazon.com/")
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.homePage.sign_in_press_button_locator()
        self.loginPage.fill_username_field("son05son28@gmail.com")
        self.loginPage.press_to_signin_button()
        time.sleep(5)
        self.loginPage.fill_password_field("Sona12345")
        time.sleep(5)
        self.loginPage.submit_button()
        time.sleep(20)
        self.actionsAndListsView = ActionsAndViewsWindow(self.driver)

        self.actionsAndListsView.move_on_accounts_and_lists_button()
        time.sleep(5)

        assert self.actionsAndListsView.heading_of_displayed_account_and_lists_window() == "Your Lists"

        self.actionsAndListsView.click_on_accounts_button()

        assert self.actionsAndListsView.title_of_the_opened_account_page() == "Your Account"

