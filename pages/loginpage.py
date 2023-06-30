from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    __username=(By.ID,"username")
    __password=(By.NAME,"pwd")
    __loginbtn=(By.XPATH,"//div[.='Login ']")
    __errormsg=(By.XPATH,"//span[contains(text(),'invalid')]")

    def __init__(self,driver):
        self.__driver=driver

    def set_username(self,un):
        self.__driver.find_element(*self.__username).send_keys(un)

    def set_password(self,pw):
        self.__driver.find_element(*self.__password).send_keys(pw)

    def click_on_loginbtn(self):
        self.__driver.find_element(*self.__loginbtn).click()

    def verify_errormsg(self,wait):
        try:
            wait.until(EC.visibility_of_element_located(self.__errormsg))
            print('error msg is displayed')
            return True
        except:
            print('error msg is not displayed')
            return False
