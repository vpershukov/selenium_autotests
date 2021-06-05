from .base_page import BasePage
from .locators import ProductPageLocators


class PageObject(BasePage):
    def add_item_to_card(self):
        add_to_card_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BTN)
        add_to_card_btn.click()

    def should_be_item_name_in_card_message(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        added_to_card_item_name = self.browser.find_element(
            *ProductPageLocators.ADDED_TO_CARD_ITEM_NAME).text

        error_info = "Item name not equal to added to card item name"

        assert item_name == added_to_card_item_name, error_info

    def should_be_item_price_in_card_info(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        added_to_card_item_price = self.browser.find_element(
            *ProductPageLocators.ADDED_TO_CARD_ITEM_PRICE).text

        error_info = "Item price not equal to added to card item price"

        assert item_price == added_to_card_item_price, error_info
