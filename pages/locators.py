from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_REGISTER = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.alert-success:nth-child(1)')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
