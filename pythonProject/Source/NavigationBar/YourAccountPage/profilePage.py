from selenium.webdriver.common.by import By
from Source.Base.base_page import BasePage

class YourProfilePage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.usernameForwardButtonLocator = (By.ID, "profile-actor-picking-form-0")
        self.profilePageUsernameTitleLocator = (By.ID, "profile-name-section")
        self.editUsernameButtonLocator = (By.ID, "name-edit-modal-link")
        self.editUsernameWindowTitleLocator = (By.CLASS_NAME, "a-popover-header-content")
        self.usernameEditButtonLocator = (By.ID, "profile-name-text-input")
        self.saveChangesButtonLocator = (By.CLASS_NAME, "a-button-text")
        self.editedUsernameTextLocator = (By.CLASS_NAME, "a-section a-spacing-micro name-edit-section-left")

    def click_username_forward_button(self):
        usernameForwardButtonElement = self.find_element(self.usernameForwardButtonLocator)
        self.click(usernameForwardButtonElement)

    def opened_profile_page_username_title(self):
        profilePageUsernameTitleElement = self.find_element(self.profilePageUsernameTitleLocator)
        title = profilePageUsernameTitleElement.text
        return title

    def click_to_edit_username_field(self):
        editUsernameButtonElement = self.find_element(self.editUsernameButtonLocator)
        self.click(editUsernameButtonElement)

    def title_of_the_displayed_edit_username_window(self):
        editUsernameWindowTitleElement = self.find_element(self.editUsernameWindowTitleLocator)
        title = editUsernameWindowTitleElement.text
        return title

    def edit_username_field(self, username):
        editUsernameFieldElement = self.find_element(self.usernameEditButtonLocator)
        editUsernameFieldElement.clear()
        self.send_keys(editUsernameFieldElement, username)

    def click_save_changes_button(self):
        saveChangesButtonElement = self.find_element(self.saveChangesButtonLocator)
        self.click(saveChangesButtonElement)

    def saved_edited_username_text(self):
        editedUsernameTextElement = self.find_element(self.editedUsernameTextLocator)
        name = editedUsernameTextElement.text
        return name

