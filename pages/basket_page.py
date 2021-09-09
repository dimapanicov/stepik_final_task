from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY),\
            "Missing message 'Basket is empty'"

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY),\
            "Basket is not empty"
