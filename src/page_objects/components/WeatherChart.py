from selene.support.jquery_style_selectors import s


class WeatherChart(object):
    def __init__(self):
        self.container = s(".weather-chart__chart-container")
        self.title = self.container.s(".title-label > div")
        self.chart = self.container.s("g.chart")
