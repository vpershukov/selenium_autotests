from .pages.product_page import PageObject


NEW_YEAR_PROMO_URL = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
NEW_YEAR_2019_PROMO_URL = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_able_to_add_item_to_card(browser):
    page = PageObject(browser, NEW_YEAR_2019_PROMO_URL)
    page.open()
    page.add_item_to_card()
    page.solve_quiz_and_get_code()
    page.should_be_item_name_in_card_message()
    page.should_be_item_price_in_card_info()
