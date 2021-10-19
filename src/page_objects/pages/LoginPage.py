import allure
from selene import browser
from selene.support.conditions import be
from selene.support.jquery_style_selectors import s

from src.page_objects.pages.DashboardPage import DashboardPage


class LoginPage(object):
    def __init__(self):
        self.email_input = s("#email")
        self.password_input = s("#password")
        self.login_button = s("#login-button__login")

    @allure.step("User login")
    def login(self, email, password):
        browser.open_url("/")
        self.email_input.set(email)
        self.password_input.set(password)
        self.login_button.click()
        DashboardPage().table_container.should(be.visible)
        return DashboardPage()
