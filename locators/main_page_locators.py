from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTION_LOCATOR = (By.XPATH, '//div[@id="accordion__heading-{}"]') # локатор для вопроса
    ANSWER_LOCATOR = (By.XPATH, '//div[@id="accordion__panel-{}"]') # локатор для ответа
    LAST_QUESTION_LOCATOR = (By.XPATH, '//div[@id="accordion__heading-7"]') # локатор последнего вопроса
    ORDER_BUTTON_HEADER = (By.XPATH, "//button[@class='Button_Button__ra12g' and contains(text(), 'Заказать')]") # верхняя кнопка "Заказать"
    ORDER_BUTTON_FOOTER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and contains(text(), 'Заказать')]") # нижняя кнопка "Заказать"
    PNG_SAMOKAT = (By.XPATH, "//img[@alt='Scooter blueprint']") # изображение самоката
    COOKIE_LOCATOR = (By.XPATH, "//button[@id= 'rcc-confirm-button' and contains(text(), 'да все привыкли')]")