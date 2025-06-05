import allure
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
#from pages.base_page import BasePage
#from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import url_main_page
from data import first_order_list
from data import second_order_list

@allure.title("Тесты на проверку создания заказов")
class TestOrderPage:

    @pytest.mark.parametrize(
        'locator, order_list',
        [
           (MainPageLocators.ORDER_BUTTON_HEADER, first_order_list),
           (MainPageLocators.ORDER_BUTTON_FOOTER, second_order_list)
        ]
    )

    @allure.description("Тест проверяет, что после заполнения полей и нажатия кнопки " \
"происходит создание заказа и появление окна 'Заказ оформлен'")
    def test_create_order(self, driver, main_page, locator, order_list):
        main_page.go_to_url(url_main_page)
        main_page.click_to_element(MainPageLocators.COOKIE_LOCATOR)
        main_page.click_to_element(locator)
        page_order = OrderPage(driver)
        page_order.set_fields_to_order(order_list)
        
        assert page_order.find_element_with_wait(OrderPageLocators.VIEW_STATUS_TITLE).is_displayed()


    @pytest.mark.parametrize(
        'locator, order_list',
        [
           (MainPageLocators.ORDER_BUTTON_HEADER, first_order_list),
           (MainPageLocators.ORDER_BUTTON_FOOTER, second_order_list)
        ]
    ) 

    @allure.description("Тест проверяет, что если нажать на логотип Яндекса, " \
    "в новом окне через редирект откроется главная страница Дзена.")
    def test_check_open_dzen_page_after_click_on_logo(self, driver, main_page, locator, order_list):
        main_page.go_to_url(url_main_page)
        main_page.click_to_element(MainPageLocators.COOKIE_LOCATOR)
        main_page.click_to_element(locator)
        page_order = OrderPage(driver)
        page_order.set_fields_to_order(order_list)
        page_order.click_to_element(OrderPageLocators.VIEW_STATUS_TITLE)
        page_order.find_element_with_wait(OrderPageLocators.LOGO_YANDEX)
        page_order.swith_to_another_window(driver) 
    
        assert page_order.find_element_with_wait(OrderPageLocators.YES_ON_MODAL_WINDOW_DZEN).is_displayed()

        # ДОБАВИТЬ ФАЙЛ REQUIREMENTS!!!!!!!!!!!!!!!!!!!!!!!!!

    @pytest.mark.parametrize(
        'locator, order_list',
        [
           (MainPageLocators.ORDER_BUTTON_HEADER, first_order_list),
           (MainPageLocators.ORDER_BUTTON_FOOTER, second_order_list)
        ]
    ) 
    @allure.description("Тест проверяет, что если нажать на логотип " \
    "«Самоката», попадёшь на главную страницу «Самоката»")
    def test_check_open_main_page_after_click_on_logo(self, driver, main_page, locator, order_list):
        main_page.go_to_url(url_main_page)
        main_page.click_to_element(MainPageLocators.COOKIE_LOCATOR)
        main_page.click_to_element(locator)
        page_order = OrderPage(driver)
        page_order.set_fields_to_order(order_list)
        page_order.find_element_with_wait(OrderPageLocators.VIEW_STATUS_TITLE)
        page_order.click_to_element(OrderPageLocators.VIEW_STATUS_TITLE)
        page_order.find_element_with_wait(OrderPageLocators.LOGO_SAMOKAT)
        page_order.click_to_element(OrderPageLocators.LOGO_SAMOKAT)

        assert page_order.find_element_with_wait(MainPageLocators.PNG_SAMOKAT).is_displayed()