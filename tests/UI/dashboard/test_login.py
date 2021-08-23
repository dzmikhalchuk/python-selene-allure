import os

from src.page_objects.pages.LoginPage import LoginPage


def test_login():
    email = os.environ['email']
    password = os.environ['password']
    (LoginPage()
     .open()
     .login(email, password)
     .table_container.is_displayed())
