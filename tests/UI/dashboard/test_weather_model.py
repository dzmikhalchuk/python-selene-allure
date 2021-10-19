import os

import pytest
import json

from selene import browser
from selene.support.conditions import be
from delayed_assert import expect, assert_expectations

from src.page_objects.pages.LoginPage import LoginPage
from src.page_objects.pages.WeatherModelPage import WeatherModelPage

with open(os.getcwd() + '/src/data/users.json') as users:
    users_data = json.load(users)


def setup():
    browser.driver().maximize_window()


@pytest.mark.parametrize("user", users_data['users'])
def test_weather_model_chart(user):
    (LoginPage()
     .login(user["email"], user["password"])
     .click_on_first_field())
    # Minimum and Maximum Temperature
    (WeatherModelPage()
     .click_on_temperature_action()
     .wait_for_chart_preloader())
    expect(WeatherModelPage().weather_chart.chart.matching(be.visible))
    expect(WeatherModelPage().weather_chart.title.text == "Minimum and Maximum Temperature")
    # Precipitation
    (WeatherModelPage()
     .click_on_precipitation_action()
     .wait_for_chart_preloader())
    expect(WeatherModelPage().weather_chart.chart.matching(be.visible))
    expect(WeatherModelPage().weather_chart.title.text == "Precipitation")
    # Soil Temperature
    (WeatherModelPage()
     .click_on_soil_temperature_action()
     .wait_for_chart_preloader())
    expect(WeatherModelPage().weather_chart.chart.matching(be.visible))
    expect(WeatherModelPage().weather_chart.title.text == "Soil Temperature (0-10cm)")
    # Relative Humidity
    (WeatherModelPage()
     .click_on_relative_humidity_action()
     .wait_for_chart_preloader())
    expect(WeatherModelPage().weather_chart.chart.matching(be.visible))
    expect(WeatherModelPage().weather_chart.title.text == "Relative Humidity")
    # Evapotranspiration
    (WeatherModelPage()
     .click_on_action_from_dropdown("Evapotranspiration")
     .wait_for_chart_preloader())
    expect(WeatherModelPage().weather_chart.chart.matching(be.visible))
    expect(WeatherModelPage().weather_chart.title.text == "Evapotranspiration")
    # Solar Radiation
    (WeatherModelPage()
     .click_on_action_from_dropdown("Solar Radiation")
     .wait_for_chart_preloader())
    expect(WeatherModelPage().weather_chart.chart.matching(be.visible))
    expect(WeatherModelPage().weather_chart.title.text == "Solar Radiation")
    # Wind Speed
    (WeatherModelPage()
     .click_on_action_from_dropdown("Wind Speed")
     .wait_for_chart_preloader())
    expect(WeatherModelPage().weather_chart.chart.matching(be.visible))
    expect(WeatherModelPage().weather_chart.title.text == "Wind Speed")
    # Growing Degree Days
    (WeatherModelPage()
     .click_on_action_from_dropdown("Growing Degree Days")
     .wait_for_chart_preloader())
    expect(WeatherModelPage().weather_chart.chart.matching(be.visible))
    expect(WeatherModelPage().weather_chart.title.text == "Growing Degree Days")
    # Assert all
    assert_expectations()


def teardown():
    browser.quit()
