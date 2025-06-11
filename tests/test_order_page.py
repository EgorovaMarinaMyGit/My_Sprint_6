import allure
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage
from data import url_main_page
from data import first_order_list
from data import second_order_list

class TestOrderPage:

    @pytest.mark.parametrize(
        'locator, order_list',
        [
           (MainPageLocators.ORDER_BUTTON_HEADER, first_order_list),
           (MainPageLocators.ORDER_BUTTON_FOOTER, second_order_list)
        ]
    )

    @allure.title("Тест проверяет, что после заполнения полей и нажатия кнопки " \
"происходит создание заказа и появление окна 'Заказ оформлен'")
    def test_create_order(self, driver, main_page, locator, order_list):
        main_page.go_to_url(url_main_page)
        main_page.click_to_cookie()
        main_page.click_to_element(locator)
        page_order = OrderPage(driver)
        page_order.set_fields_to_order(order_list)
        
        assert page_order.check_visibility_of_view_status_button()


    @pytest.mark.parametrize(
        'locator, order_list',
        [
           (MainPageLocators.ORDER_BUTTON_HEADER, first_order_list),
           (MainPageLocators.ORDER_BUTTON_FOOTER, second_order_list)
        ]
    ) 

    @allure.title("Тест проверяет, что если нажать на логотип Яндекса, " \
    "в новом окне через редирект откроется главная страница Дзена.")
    def test_check_open_dzen_page_after_click_on_logo(self, driver, main_page, locator, order_list):
        main_page.go_to_url(url_main_page)
        main_page.click_to_cookie()
        main_page.click_to_element(locator)
        page_order = OrderPage(driver)
        page_order.set_fields_to_order(order_list)
        page_order.click_to_yandex_logo_and_switch_to_dzen()
    
        assert page_order.check_visibility_of_dzen()


    @pytest.mark.parametrize(
        'locator, order_list',
        [
           (MainPageLocators.ORDER_BUTTON_HEADER, first_order_list),
           (MainPageLocators.ORDER_BUTTON_FOOTER, second_order_list)
        ]
    ) 
    @allure.title("Тест проверяет, что если нажать на логотип " \
    "«Самоката», попадёшь на главную страницу «Самоката»")
    def test_check_open_main_page_after_click_on_logo(self, driver, main_page, locator, order_list):
        main_page.go_to_url(url_main_page)
        main_page.click_to_cookie()
        main_page.click_to_element(locator)
        page_order = OrderPage(driver)
        page_order.set_fields_to_order(order_list)
        page_order.click_to_samokat_logo_and_switch_to_main_page()

        assert page_order.check_visibility_of_samokat_png()