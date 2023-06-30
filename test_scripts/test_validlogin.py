import time

import pytest

from generic.base_test import BaseTest
from generic.utility import Excel
from pages.homepage import HomePage
from pages.loginpage import LoginPage


class TestValidLogin(BaseTest):
    @pytest.mark.run(order=1)
    def test_validlogin(self):
        try:
            un = Excel.get_cellvalue("../data/input.xlsx", "Validlogin", 2,1)
            pw = Excel.get_cellvalue("../data/input.xlsx", "Validlogin", 2,2)
        except:

            un = Excel.get_cellvalue("data/input.xlsx", "Validlogin", 2,1)
            pw = Excel.get_cellvalue("data/input.xlsx", "Validlogin", 2,2)

        loginpage = LoginPage(self.driver)
        loginpage.set_username(un)
        loginpage.set_password(pw)
        loginpage.click_on_loginbtn()
        homepage=HomePage(self.driver)
        result=homepage.verify_homepage_is_displayed(self.wait)
        assert result
        print(self.driver.title)


