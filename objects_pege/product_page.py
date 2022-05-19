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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *TestProductPagesLocators.MESSAGE_ADD), "Success message is presented, but should not be"

    def should_not_be_is_disappeared(self):
        assert self.is_disappeared(
            *TestProductPagesLocators.MESSAGE_ADD), "Success message is presented, but should not be"
