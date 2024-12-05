from POM_Login.login import Login
import pytest


@pytest.mark.usefixtures("setup")
class Test_Login:
    def test_login(self, setup):
        object = Login(setup)
        object.login("Admin", "admin123")
        object.logout()