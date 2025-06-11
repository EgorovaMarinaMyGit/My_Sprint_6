import allure
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from data import url_main_page
from data import answers_list

class TestMainPage:
    
    @allure.title("Тест проверяет, что когда нажимаешь на вопрос, открывается соответствующий " \
"текст ответа")

    @pytest.mark.parametrize('num', [0,1,2,3,4,5,6,7])

    def test_answer_question(self, main_page, num): 
        main_page.go_to_url(url_main_page)
        main_page.click_to_question(num)
        assert main_page.get_answer_on_question(num) == answers_list[num]
    