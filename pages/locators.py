from selenium.webdriver.common.by import By


class BasePageVar():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.CSS_SELECTOR, ".basket-mini span.btn-group")


class CartPageVar():
    CART_CONTAINS = (By.CSS_SELECTOR, "#content_inner p")
    CART_CONTAINS_SOME_PRODUCT = (By.CSS_SELECTOR, "h3.price_color")


class MainPageLocators:
    pass


class LoginPageVar:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-primary")


class TestProductPagesLocators:
    ADD_PRODUCT = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_ADD = (By.CSS_SELECTOR, "div#messages  div:first-child .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "{{Some locator}}")
