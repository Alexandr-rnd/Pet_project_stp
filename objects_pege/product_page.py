from objects_pege.locators import TestProductPagesLocators
from objects_pege.base_page import BasePage

class TestProductPages(BasePage):
    def press_button_add_to_basket(self):
        login_link = self.browser.find_element(*TestProductPagesLocators.ADD_PRODUCT)
        login_link.click()

    def should_be_message_about_adding(self):
        product_name = self.browser.find_element(*TestProductPagesLocators.PRODUCT_NAME).text
        message_name = self.browser.find_element(*TestProductPagesLocators.MESSAGE_ADD).text
        assert message_name == product_name, "product name not true"

    def should_be_message_basket_total(self):
        message_basket_total = self.browser.find_element(*TestProductPagesLocators.MESSAGE_BASKET).text
        product_price = self.browser.find_element(*TestProductPagesLocators.PRODUCT_PRICE).text
        assert product_price == message_basket_total, "Total price not true"