from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator) 
    
    def click_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def add_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text
    
    def formatted_locator(self, f_locator, num):
        method, locator = f_locator
        locator = locator.format(num)
        return method, locator
    
    def wait_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator) 
    
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element) 