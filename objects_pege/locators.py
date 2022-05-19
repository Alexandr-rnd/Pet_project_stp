from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class TestProductPagesLocators():
    ADD_PRODUCT = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_ADD = (By.CSS_SELECTOR, "div#messages  div:first-child .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")