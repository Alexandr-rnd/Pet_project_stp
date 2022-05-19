from pages.base_page import BasePage
from pages.locators import CartPageVar


class BascketPage(BasePage):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def in_cart_should_not_product(self):
        message_product_in_cart = self.browser.find_element(*CartPageVar.CART_CONTAINS).text
        assert "Your basket is empty." in message_product_in_cart, "Total price not true"

    def in_cart_should_not_present_some_product(self):
        assert self.is_not_element_present(
            *CartPageVar.CART_CONTAINS_SOME_PRODUCT), "Some product is presented, but should not be"
