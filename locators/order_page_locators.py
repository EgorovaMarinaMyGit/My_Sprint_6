from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']") # поле "* Имя"
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']") # поле "* Фамилия"
    ADRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") # поле "* Адрес: куда привезти заказ"
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']") # поле "* Станция метро"
    STATION_LIST = (By.CLASS_NAME, 'select-search__select')
    TELEPHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") # поле "* Телефон: на него позвонит курьер"
    NEXT_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and contains(text(), 'Далее')]") # кнопка "Далее"
    ABOUT_RENT_TITLE = (By.XPATH, "//div[@class='Order_Header__BZXOb' and contains(text(), 'Про аренду')]") # надпись "Про аренду"
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") # поле "* Когда привезти самокат"
    DATE_IN_CALENDAR = (By.XPATH, "//div[@aria-label='Choose понедельник, 23-е июня 2025 г.']")
    RENTAL_PERIOD_FIELD = (By.XPATH, "//div[@class='Dropdown-placeholder']") # поле "* Срок аренды"
    DAYS_OF_RENT = (By.XPATH, "//div[@class='Dropdown-menu']")
    BLACK_COLOR_CHECKBOX = (By.XPATH, "//label[@for='black']") # чекбокс "чёрный жемчуг"
    GRAY_COLOR_CHECKBOX = (By.XPATH, "//label[@for='grey']") # чекбокс "серая безысходность"
    COMMENT_FOR_COURIER_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") # поле "* Комментарий для курьера"
    YES_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]") # кнопка "Да"
    ORDER_PLACED_TITLE = (By.XPATH, "//div[@class='Order-Text__2broi' and contains(text(), 'Номер заказа')]")
    VIEW_STATUS_TITLE = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]") # кнопка "Посмотреть статус"
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']") # лого Яндекс
    LOGO_SAMOKAT = (By.XPATH, "//img[@alt='Scooter']") # лого Самокат
    LOGO_DZEN = (By.XPATH, "//path[@fill='#202022']") # лого Дзена (звёздочка)
    YES_ON_MODAL_WINDOW_DZEN = (By.XPATH, "//a[@title='Да']")