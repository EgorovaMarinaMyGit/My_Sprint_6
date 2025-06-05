import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Клик на вопрос")
    def click_to_question(self, num): 
        question_with_num = self.formatted_locator(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.LAST_QUESTION_LOCATOR)
        self.click_to_element(question_with_num)

    @allure.step("Получение ответа на вопрос")
    def get_answer_on_question(self, num):
        answer_with_num = self.formatted_locator(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(answer_with_num)
    
    @allure.step("Проверка ответа")
    def check_answer_on_question(self, num, expected_text):
        self.click_to_question(num)
        text = self.get_answer_on_question(num)
        return text == expected_text