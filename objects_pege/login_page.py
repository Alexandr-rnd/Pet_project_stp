from objects_pege.base_page import BasePage
from objects_pege.locators import LoginPageVar
from objects_pege.locators import BasePageVar
from faker import Faker


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

    def register_new_user(self):
        f = Faker()
        pass1 = f.password()
        email_user = self.browser.find_element(*LoginPageVar.EMAIL_INPUT)
        password_user = self.browser.find_element(*LoginPageVar.PASSWORD_INPUT)
        confirm_user = self.browser.find_element(*LoginPageVar.CONFIRM_INPUT)
        email_user.send_keys(f.email())
        password_user.send_keys(pass1)
        confirm_user.send_keys(pass1)
        button = self.browser.find_element(*LoginPageVar.REGISTER_BUTTON)
        button.click()
