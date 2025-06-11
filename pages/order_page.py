import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):


    @allure.step('Создание заказа')
    def set_fields_to_order(self, order_list):
        self.add_text_to_element(OrderPageLocators.NAME_FIELD, order_list['имя'])
        self.add_text_to_element(OrderPageLocators.SURNAME_FIELD, order_list['фамилия'])
        self.add_text_to_element(OrderPageLocators.ADRESS_FIELD, order_list['адрес'])
        self.click_to_element(OrderPageLocators.METRO_FIELD)
        self.add_text_to_element(OrderPageLocators.METRO_FIELD, "Черкизовская")
        self.click_to_element(OrderPageLocators.STATION_LIST)
        self.add_text_to_element(OrderPageLocators.TELEPHONE_FIELD, order_list['телефон'])
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)
        self.find_element_with_wait(OrderPageLocators.ABOUT_RENT_TITLE)
        self.click_to_element(OrderPageLocators.DATE_FIELD)
        self.click_to_element(OrderPageLocators.DATE_IN_CALENDAR)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click_to_element(OrderPageLocators.DAYS_OF_RENT)
        self.click_to_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        self.add_text_to_element(OrderPageLocators.COMMENT_FOR_COURIER_FIELD, order_list['комментарий для курьера'])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_FOOTER)
        self.find_element_with_wait(OrderPageLocators.YES_BUTTON)
        self.click_to_element(OrderPageLocators.YES_BUTTON)


    @allure.step('Проверка, что при успешном оформлении заказа появляется модальное окно 
    'с кнопкой Посмотреть заказ')
    def check_visibility_of_view_status_button(self):
        self.find_element_with_wait(OrderPageLocators.VIEW_STATUS_TITLE).is_displayed()


    @allure.step('Проверка, что после нажатия на "Показать заказ" и потом на лого Яндекса ' \
    'происходит переход на страницу Дзен Яндекс')
    def click_to_yandex_logo_and_switch_to_dzen(self):
        self.click_to_element(OrderPageLocators.VIEW_STATUS_TITLE)
        self.find_element_with_wait(OrderPageLocators.LOGO_YANDEX)
        self.swith_to_another_window(OrderPageLocators.LOGO_YANDEX)


    @allure.step('Проверка, что при переходе на сайт Дзен Яндекс появляется модальное окно ' \
    'на скачивание Яндекс браузера')   
    def check_visibility_of_dzen(self):
        self.find_element_with_wait(OrderPageLocators.YES_ON_MODAL_WINDOW_DZEN).is_displayed()


    @allure.step('Проверка, что после нажатия на "Показать заказ" и потом на лого Самоката ' \
    'происходит переход на главную страницу Самоката')
    def click_to_samokat_logo_and_switch_to_main_page(self):
        self.find_element_with_wait(OrderPageLocators.VIEW_STATUS_TITLE)
        self.click_to_element(OrderPageLocators.VIEW_STATUS_TITLE)
        self.find_element_with_wait(OrderPageLocators.LOGO_SAMOKAT)
        self.click_to_element(OrderPageLocators.LOGO_SAMOKAT)


    @allure.step('Проверка, что при переходе на главную страницу Самоката Яндекс отображется ' \
    'лого самоката')
    def check_visibility_of_samokat_png(self):
        self.find_element_with_wait(OrderPageLocators.PNG_SAMOKAT).is_displayed()


    