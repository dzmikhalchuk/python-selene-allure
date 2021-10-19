from selene.support.conditions import be
from selene.support.jquery_style_selectors import s

from src.page_objects.components.WeatherChart import WeatherChart


class WeatherModelPage(object):
    def __init__(self):
        self.min_max_temperature_button = s("#temperature_t2m-tab__weather-model")
        self.precipitation_button = s("#precipitation-tab__weather-model")
        self.soil_temperature_button = s("#soil_temperature-tab__weather-model")
        self.relative_humidity_button = s("#relative_humidity-tab__weather-model")
        self.evapotranspiration_button = s("#evapotranspiration-tab__weather-model")
        self.chart_actions_dropdown_button = s(".chart-actions__dropdown-button")
        self.chart_actions_dropdown = s(".control-item")
        self.chart_preloader = s(".weather-chart__preload-container")
        self.weather_chart = WeatherChart()

    def click_on_temperature_action(self):
        self.min_max_temperature_button.should(be.visible)
        self.min_max_temperature_button.click()
        return self

    def click_on_precipitation_action(self):
        self.precipitation_button.should(be.visible)
        self.precipitation_button.click()
        return self

    def click_on_soil_temperature_action(self):
        self.soil_temperature_button.should(be.visible)
        self.soil_temperature_button.click()
        return self

    def click_on_relative_humidity_action(self):
        self.relative_humidity_button.should(be.visible)
        self.relative_humidity_button.click()
        return self

    def click_on_evapotranspiration_action(self):
        self.evapotranspiration_button.should(be.visible)
        self.evapotranspiration_button.click()
        return self

    def click_on_action_from_dropdown(self, action_name):
        locator = '//*[@class="control-item"]//div[text()="{}"]'
        self.chart_actions_dropdown_button.should(be.clickable)
        self.chart_actions_dropdown_button.click()
        elem = s(locator.format(action_name))
        elem.should(be.visible)
        elem.click()
        return self

    def wait_for_chart_preloader(self):
        # self.chart_preloader.should(be.visible)
        self.chart_preloader.should(be.hidden)
