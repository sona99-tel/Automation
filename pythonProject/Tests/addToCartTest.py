from Source.cartPage import CartPage
from Source.NavigationBar.navigationBar import NavigationBar
from Source.searchResultPage import SearchResultElementPage
from Source.productDetailsPage import ProductDetails
from Tests.base_test.base_test import BaseTest

class CartAddTest(BaseTest):

    def test_add_item_to_card(self):
        self.driver.get("https://www.amazon.com/")
        self.cartPage = CartPage(self.driver)
        self.productDetailsPage = ProductDetails(self.driver)
        self.navigationBar = NavigationBar(self.driver)
        self.searchResultPage = SearchResultElementPage(self.driver)
        self.navigationBar.fill_search_field('iphone 14')
        self.navigationBar.submit_search_button()
        self.searchResultPage.click_on_first_element()
        self.productDetailsPage.adding_cart_button_locator()

        assert self.driver.title == "Amazon.com Shopping Cart"

