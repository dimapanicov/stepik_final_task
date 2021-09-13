from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_link.click()

    def price_match(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        basket_price = basket_price.text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = product_price.text
        assert product_price == basket_price, 'Basket and product have different prices'

    def name_match(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product_name.text
        product_in_bascet = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET)
        product_in_bascet = product_in_bascet.text
        assert product_name == product_in_bascet, "Product name don't match with product in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"


