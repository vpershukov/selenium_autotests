from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        empty_basket = self.is_not_element_presented(
            *BasketPageLocators.BASKET_WO_ITEMS)

        assert empty_basket == True, "Basket is not empty"

    def should_be_empty_basket_info(self):
        empty_basket_info = self.browser.find_element(
            *BasketPageLocators.EMPTY_BASKET_INFO).text
        empty_basket_message = "Ваша корзина пуста"
        error_ifo = "Basket is not empty or basket message is wrong"

        assert empty_basket_message in empty_basket_info, error_ifo
