from Source.loginPage import LoginPage
from Source.NavigationBar.accountsAndListsView import ActionsAndViewsWindow
from Source.homePage import HomePage
from Tests.base_test.base_test import BaseTest
from Source.NavigationBar.YourAccountPage.accountPage import YourAccountPage
from Source.NavigationBar.YourAccountPage.profilePage import YourProfilePage
from Source.NavigationBar.YourAccountPage.ordersPage import YourOrdersPage
import time

class TestCase(BaseTest):

    def test_orders_page(self):
        self.driver.get("https://www.amazon.com/")
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.actionsAndListsView = ActionsAndViewsWindow(self.driver)
        self.accountPage = YourAccountPage(self.driver)
        self.profilePage = YourProfilePage(self.driver)
        self.ordersPage = YourOrdersPage(self.driver)
        self.homePage.sign_in_press_button_locator()
        self.loginPage.fill_username_field("son05son28@gmail.com")
        self.loginPage.press_to_signin_button()
        time.sleep(2)
        self.loginPage.fill_password_field("Sona12345")
        time.sleep(2)
        self.loginPage.submit_button()
        time.sleep(2)
        self.actionsAndListsView.move_on_accounts_and_lists_button()
        time.sleep(2)
        self.actionsAndListsView.click_on_accounts_button()
        self.accountPage.click_your_orders_button()
        time.sleep(2)

        assert self.driver.title == "Your Orders"

        self.ordersPage.click_cancelled_orders_button()
        time.sleep(2)


        assert self.ordersPage.get_message_in_cancelled_orders_page() == "We aren't finding any cancelled orders (for orders placed in the last 6 months)."

