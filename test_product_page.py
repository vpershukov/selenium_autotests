import pytest


from .pages.product_page import PageObject
from .pages.login_page import LoginPage


CODERS_AT_WORK = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
CITY_AND_STARS = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.parametrize(
    "promo_code",
    [
        "offer0", "offer1", "offer2", "offer3", "offer4",
        "offer5", "offer6", pytest.param("offer7", marks=pytest.mark.skip),
        "offer8", "offer9"
    ]
)
def test_guest_able_to_add_item_to_card(browser, promo_code):
    URL = f"{CODERS_AT_WORK}?promo={promo_code}"
    page = PageObject(browser, URL)
    page.open()
    page.add_item_to_card()
    page.solve_quiz_and_get_code()
    page.should_be_item_name_in_card_message()
    page.should_be_item_price_in_card_info()


def test_guest_cant_see_success_message(browser):
    page = PageObject(browser, CODERS_AT_WORK)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip(reason="Negative test for task")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = PageObject(browser, CODERS_AT_WORK)
    page.open()
    page.add_item_to_card()
    page.should_not_be_success_message()


@pytest.mark.skip(reason="Negative test for task")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = PageObject(browser, CODERS_AT_WORK)
    page.open()
    page.add_item_to_card()
    page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = PageObject(browser, CITY_AND_STARS)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = PageObject(browser, CITY_AND_STARS)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# TO DO
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    pass
