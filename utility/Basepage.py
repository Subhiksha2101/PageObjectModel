from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Basepage:

    def __init__(self, driver):
        self.driver = driver

    def hrm_send_keys(self, locator, text):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def hrm_btn_click(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)).click()

    def hrm_get_title(self, title):
        WebDriverWait(self.driver, 30).until(EC.title_is(title))
        return self.driver.title

    def hrm_click_link(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)).click()