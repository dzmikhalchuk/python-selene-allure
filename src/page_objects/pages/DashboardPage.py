import allure
from selene.support.conditions import be
from selene.support.jquery_style_selectors import s, ss

from src.page_objects.pages.WeatherModelPage import WeatherModelPage


class DashboardPage(object):
    def __init__(self):
        self.table_container = s(".table__content")
        self.field_cells = ss("[id*='field-name__table']")

    @allure.step("Click on Field")
    def click_on_first_field(self):
        self.field_cells.first().should(be.visible)
        self.field_cells.first().click()
        return WeatherModelPage()
