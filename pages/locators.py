from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inv")
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")


class MainPageLocators():
    REGISTER_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGSTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CARD_BTN = (
        By.CSS_SELECTOR,
        ".btn.btn-lg.btn-primary.btn-add-to-basket"
    )
    ITEM_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    ADDED_TO_CARD_ITEM_NAME = (By.CSS_SELECTOR, ".page_inner .alert-success strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADDED_TO_CARD_ITEM_PRICE = (By.CSS_SELECTOR, ".page_inner .alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".page_inner .alert-success")


class BasketPageLocators():
    EMPTY_BASKET_INFO = (By.CSS_SELECTOR, ".content p")
    BASKET_WO_ITEMS = (By.ID, "#basket_formset")
