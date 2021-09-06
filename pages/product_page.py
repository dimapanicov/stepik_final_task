from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_link.click()
        BasePage.solve_quiz_and_get_code(self)

    def price_match(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        basket_price = basket_price.text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = product_price.text
        assert product_price in basket_price, 'basket and prodect have difrent price'

    def name_match(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product_name.text
        product_in_bascet = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET)
        product_in_bascet = product_in_bascet.text
        assert product_name in product_in_bascet, "product_name don't match with product in basket"