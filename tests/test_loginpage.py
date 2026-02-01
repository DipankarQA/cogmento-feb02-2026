from page.loginpage import LoginPage
import pytest
from utils.excelreader import excelreader

er = excelreader(r"C:\Dipankar\VS\cogmento 1st-feb-2026\testdata.xlsx", "Sheet1")
@pytest.mark.parametrize("user,password", er)
def test_loginpage(page,user,password):
    l = LoginPage(page)
    l.login_verify(user, password)