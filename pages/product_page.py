from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_link.click()
        BasePage.solve_quiz_and_get_code(self)

    def price_match(self):
        pass

    def name_match(self):
        pass
