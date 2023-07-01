import pytest

from generic.base_test import BaseTest
from generic.utility import Excel
from pages.loginpage import LoginPage


class TestInValidLogin(BaseTest):
    @pytest.mark.run(order=2)
    def test_invalidlogin(self):
        try:
            un=Excel.get_cellvalue("../data/input.xlsx","Invalidlogin",2,1)
            pw=Excel.get_cellvalue("../data/input.xlsx","Invalidlogin",2,2)
        except:
            un = Excel.get_cellvalue("data/input.xlsx", "Invalidlogin", 2, 1)
            pw = Excel.get_cellvalue("data/input.xlsx", "Invalidlogin", 2, 2)

        loginpage=LoginPage(self.driver)
        loginpage.set_password(un)
        loginpage.set_password(pw)
        loginpage.click_on_loginbtn()
        result=loginpage.verify_errormsg(self.wait)
        assert result
        print(self.driver.title)
