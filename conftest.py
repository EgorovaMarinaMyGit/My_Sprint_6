import pytest
from selenium import webdriver
from data import url_main_page
from data import url_order_page
from pages.main_page import MainPage
from pages.order_page import OrderPage

# для браузера + выход
@pytest.fixture
def driver():
    firefox = webdriver.Firefox()
    firefox.maximize_window()
    yield firefox
    firefox.quit()

# фикстура для главной страницы
@pytest.fixture
def main_page(driver):
    page_main = MainPage(driver)
    return page_main

# фикстура для страницы заказа
@pytest.fixture
def order_page(driver):
    page_order = OrderPage(driver)
    return page_order