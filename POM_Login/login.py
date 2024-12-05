import time

from selenium.webdriver.common.by import By
from utility.Basepage import Basepage


class Login(Basepage):
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    submit = (By.CSS_SELECTOR, ".oxd-button")
    clik_name = (By.CSS_SELECTOR, ".oxd-userdropdown-name")
    Logout = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, namevalue, pwdvalue):
        self.hrm_send_keys(self.username, namevalue)
        self.hrm_send_keys(self.password, pwdvalue)
        self.hrm_btn_click(self.submit)
        time.sleep(5)

    def logout(self):
        self.hrm_btn_click(self.clik_name)
        self.hrm_btn_click(self.Logout)
        time.sleep(5)

    def get_title(self, title):
        self.hrm_get_title(title)