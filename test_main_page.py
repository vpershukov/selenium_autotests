from .pages.main_page import MainPage
from .pages.login_page import LoginPage


LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
MIDSUMMER_PROMO_URL = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=midsummer"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MIDSUMMER_PROMO_URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MIDSUMMER_PROMO_URL)
    page.open()
    page.should_be_login_link()


def test_guest_should_see_current_login_page(browser):
    page = LoginPage(browser, LOGIN_URL)
    page.open()
    page.should_be_login_page()
