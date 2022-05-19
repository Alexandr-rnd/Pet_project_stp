from objects_pege.main_page import MainPage
from objects_pege.login_page import LoginPage
from objects_pege.bascket_page import BascketPage

LINK = "http://selenium1py.pythonanywhere.com"


class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = LINK
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = LINK
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart()
    cart_page = BascketPage(browser, browser.current_url)
    cart_page.in_cart_should_not_product()
    cart_page.in_cart_should_not_present_some_product()
