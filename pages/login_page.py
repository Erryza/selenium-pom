
from .base_page import BasePage
from locators.login_locators import LoginPageLocators


class LoginPage(BasePage):
    def navigate_url(self, url):
        self.navigate_to(url)

    def enter_username(self, username):
        self.enter_el_text(LoginPageLocators.USERNAME, username)

    def enter_password(self, password):
        self.enter_el_text(LoginPageLocators.PASSWORD, password)

    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def get_title(self):
        return self.get_el_title()

    def get_text(self):
        self.get_el_text(LoginPageLocators.MESSAGE)

    def get_message(self, actual, expected):
        self.get_el_message(actual, expected)
