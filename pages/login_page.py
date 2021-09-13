from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.browser.current_url, 'There is no login url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'There is no login form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER), 'There is no register_form'

    def register_new_user(self):
        generate_email = str(time.time()) + "@fakemail.org"
        generate_password = str(time.time())
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(generate_email)
        password_field1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password_field1.send_keys(generate_password)
        password2_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password2_field.send_keys(generate_password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT).click()
