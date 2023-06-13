from Source.loginPage import LoginPage
from Source.navigationBar import NavigationBar
from Source.cartPage import CartPage
from Source.homePage import HomePage
from Source.searchResultPage import SearchResultElementPage
from Tests.base_test.base_test import BaseTest

class TestCase(BaseTest):
    def test_login_test(self):
        self.driver.get("https://www.amazon.com/")
        self.loginPage = LoginPage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.searchResultPage = SearchResultElementPage(self.driver)
        self.homePage.sign_in_press_button_locator()
        self.loginPage.fill_username_field("son05son28@gmail.com")
        self.loginPage.press_to_signin_button()
        self.loginPage.fill_password_field("Sona12345")
        self.loginPage.submit_button()
        self.navigationBar = NavigationBar(self.driver)
        self.navigationBar.fill_search_field('iphone 14')
        self.navigationBar.submit_search_button()
        self.searchResultPage.click_on_first_element()

        assert self.driver.title == "Amazon.com Shopping Cart"

