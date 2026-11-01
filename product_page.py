from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_success_message_with_product_name(self, expected_name):
        success_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert success_name == expected_name, \
            f"Product name mismatch: expected='{expected_name}', message='{success_name}'"

    def should_be_basket_total_equal_to_price(self, expected_price):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert basket_total == expected_price, \
            f"Basket total mismatch: expected='{expected_price}', total='{basket_total}'"