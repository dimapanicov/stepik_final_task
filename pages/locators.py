from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_REGISTER = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-add-to-basket')

    BASKET_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')

    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.alert-success:nth-child(1) strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-child(1)')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_LINK= (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, ".content #content_inner p")
    BASKET_SUMMARY = (By.CSS_SELECTOR, ".basket_summary")
