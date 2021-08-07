from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        empty_basket = self.is_not_element_presented(
            *BasketPageLocators.BASKET_WO_ITEMS)

        assert empty_basket == True, "Basket is not empty"

    def should_be_empty_basket_info(self):
        empty_basket_info = self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_INFO)

        assert empty_basket_info == True, "Basket is not empty"
