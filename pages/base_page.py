import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, method, css_selector):
        try:
            self.browser.find_element(method, css_selector)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_presented(self, method, css_selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((method, css_selector))
            )
        except TimeoutException:
            return True
        return False

    def is_element_disappeared(self, method, css_selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((method, css_selector))
            )
        except TimeoutException:
            return False
        return True

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_basket_btn(self):
        assert self.is_element_present(
            *BasePageLocators.BASKET_BTN), "Basket button is not presented"

    def go_to_basket(self):
        basket = self.browser.find_element(*BasePageLocators.BASKET_BTN)
        basket.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_authorized_user(self):
        error_info = "User icon is not presented, probably unauthorised user"
        assert self.is_element_present(*BasePageLocators.USER_ICON), error_info
