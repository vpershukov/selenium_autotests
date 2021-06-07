import string
import random
from selenium.webdriver.common.by import By


from .base_page import BasePage
from .locators import LoginPageLocators, BasketPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "Wrong login page URL"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGSTER_FORM), "Register form is not presented"

    def random_string(self, size=5):
        return "".join(random.choice(string.ascii_lowercase) for _ in range(size))

    def random_email(self):
        name = self.random_string()
        second_level_domain = self.random_string(size=5)
        top_level_domain = self.random_string(size=3)
        email_address = f"{name}@{second_level_domain}.{top_level_domain}"

        return email_address

    def register_new_user(self):
        email = self.random_email()
        password = self.random_string(size=10)
        email_field = self.browser.find_element(
            *BasketPageLocators.REGISTER_USER_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(
            *BasketPageLocators.REGISTER_USER_PASS)
        password_field.send_keys(password)
        password_field_confirm = self.browser.find_element(
            *BasketPageLocators.REGISTER_USER_PASS_CONFIRM)
        password_field_confirm.send_keys(password)

        register = self.browser.find_element(*BasketPageLocators.REGISTER_BTN)
        register.click()
