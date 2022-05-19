from objects_pege.base_page import BasePage
from objects_pege.locators import LoginPageVar
from objects_pege.locators import BasePageVar


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.find_element(*BasePageVar.LOGIN_LINK)
        login_link.click()
        assert "login" in self.browser.current_url, "Login link is not correct"

    def should_be_login_form(self):
        login_link = self.browser.find_element(*BasePageVar.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageVar.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        login_link = self.browser.find_element(*BasePageVar.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageVar.REGISTER_FORM), "register form is not presented"
