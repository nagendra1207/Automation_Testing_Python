import pytest
from conftest import *
from hrmpages.login import LoginPage


@pytest.mark.userfixtures("browser_setup")
class Test_login:

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        self.login_page.login(username,password)

    def teardown_class(self):
        self.driver.quit()

