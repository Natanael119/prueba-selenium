import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


base_Url = "https://v2.psicoalianza.com/"


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.rounded_1 = "//INPUT[@id='email']"
        self.rounded_2 = "//INPUT[@id='password']"
        self.rounded_3 = "//BUTTON[@type='submit'][text()='Iniciar sesión']"








    def get_rounded_1(self):
        return self.driver.find_element(By.XPATH, self.rounded_1)

    def get_rounded_2(self):
        return self.driver.find_element(By.XPATH, self.rounded_2)

    def get_rounded_3(self):
        return self.driver.find_element(By.XPATH, self.rounded_3)









 ##metodos acciones elementos
    def sing_up(self,rounded_1,rounded_2,rounded_3):

        self.get_rounded_1().send_keys(rounded_1)
        self.get_rounded_1().send_keys(Keys.TAB)
        self.get_rounded_2().send_keys(rounded_2)
        self.get_rounded_3().send_keys(rounded_3)


        time.sleep(3)


    def click_sing_up(self):
        self.get_rounded_3().click()









    @staticmethod
    def get_base_url():
        return base_Url