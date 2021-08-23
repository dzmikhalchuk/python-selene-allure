from selene.support.jquery_style_selectors import s


class DashboardPage(object):
    def __init__(self):
        self.table_container = s(".table__content")
