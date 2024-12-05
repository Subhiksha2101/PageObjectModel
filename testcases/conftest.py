import time

import pytest
from selenium import webdriver


@pytest.fixture(scope="class", params=["chrome", "firefox"])
def setup(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(4)
    if request.param == "firefox":
        driver = webdriver.Firefox()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(4)
    if request.param == "IE":
        driver = webdriver.Edge()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(4)

    request.cls.driver = driver
    yield driver
    driver.close()


