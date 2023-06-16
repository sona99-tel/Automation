from Source.loginPage import LoginPage
from Source.NavigationBar.accountsAndListsView import ActionsAndViewsWindow
from Source.homePage import HomePage
from Tests.base_test.base_test import BaseTest
from Source.NavigationBar.YourAccountPage.accountPage import YourAccountPage
from Source.NavigationBar.YourAccountPage.profilePage import YourProfilePage
import time

class TestCase(BaseTest):

    def test_yor_profile_page(self):
        self.driver.get("https://www.amazon.com/")
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.actionsAndListsView = ActionsAndViewsWindow(self.driver)
        self.accountPage = YourAccountPage(self.driver)
        self.profilePage = YourProfilePage(self.driver)
        self.homePage.sign_in_press_button_locator()
        self.loginPage.fill_username_field("son05son28@gmail.com")
        self.loginPage.press_to_signin_button()
        time.sleep(2)
        self.loginPage.fill_password_field("Sona12345")
        time.sleep(2)
        self.loginPage.submit_button()
        time.sleep(5)
        self.actionsAndListsView.move_on_accounts_and_lists_button()
        time.sleep(5)
        self.actionsAndListsView.click_on_accounts_button()
        self.accountPage.click_your_profile_button()

        assert self.accountPage.title_of_profile_page() == "Manage your Profiles"

        self.profilePage.click_username_forward_button()

        assert self.profilePage.opened_profile_page_username_title() == "Test"

        self.profilePage.click_to_edit_username_field()
        time.sleep(2)

        assert self.profilePage.title_of_the_displayed_edit_username_window() == "Edit your name"

        assert self.profilePage.title_of_the_displayed_edit_username_window() == "Edit your name"
        self.profilePage.edit_username_field("Test123")

        self.profilePage.click_save_changes_button()
        time.sleep(2)

        assert self.profilePage.saved_edited_username_text() == "Test123"


