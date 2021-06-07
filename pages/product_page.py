from .base_page import BasePage
from .locators import ProductPageLocators


class PageObject(BasePage):
    def add_item_to_card(self):
        add_to_card_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BTN)
        add_to_card_btn.click()

    def get_item_name(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text

    def get_added_to_card_item_name(self):
        return self.browser.find_element(
            *ProductPageLocators.ADDED_TO_CARD_ITEM_NAME).text

    def get_item_price(self):
        return self.browser.find_element(
            *ProductPageLocators.ITEM_PRICE).text

    def get_item_price_in_card_info(self):
        return self.browser.find_element(
            *ProductPageLocators.ADDED_TO_CARD_ITEM_PRICE).text

    def should_be_item_name_in_card_message(self):
        item_name = self.get_item_name()
        added_to_card_item_name = self.get_added_to_card_item_name()
        error_info = "Item name not equal to added to card item name"

        assert item_name == added_to_card_item_name, error_info

    def should_be_item_price_in_card_info(self):
        item_price = self.get_item_price()
        added_to_card_item_price = self.get_item_price_in_card_info()
        error_info = "Item price not equal to added to card item price"

        assert item_price == added_to_card_item_price, error_info

    def should_not_be_success_message(self):
        """Should not be success message before item added to the basket"""
        success_message = self.is_not_element_presented(
            *ProductPageLocators.SUCCESS_MESSAGE
        )

        assert success_message == True, "Success message is presented"

    def should_be_disappeared_success_message(self):
        """Success message should disappeare after item added to the basket"""
        success_message = self.is_element_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        )

        assert success_message == True, "Success message is not disappeared"
