from Source.cartPage import CartPage
from Source.NavigationBar.navigationBar import NavigationBar
from Source.loginPage import LoginPage
from Source.homePage import HomePage
from Tests.base_test.base_test import BaseTest
import time

class DeleteOfItemTest(BaseTest):

    def test_deleting_item(self):
        self.driver.get("https://www.amazon.com/")
        self.cartPage = CartPage(self.driver)
        self.navigationBar = NavigationBar(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.homePage.sign_in_press_button_locator()
        self.loginPage.fill_username_field("son05son28@gmail.com")
        self.loginPage.press_to_signin_button()
        self.loginPage.fill_password_field("Sona12345")
        time.sleep(10)
        self.loginPage.submit_button()
        self.navigationBar.click_to_cart_button()
        self.cartPage.click_to_delete_item()

        assert self.cartPage.get_success_message_of_deletion() == "Apple iPhone 14, 256GB, Midnight - Unlocked (Renewed Premium)"