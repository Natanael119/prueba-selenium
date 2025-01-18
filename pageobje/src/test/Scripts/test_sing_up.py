import time



from src.pageObject.pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.pageObject.pages.HomePage import HomePage

class Test_course_pack(WebDriverSetup):

    def test_add_item_to_course_pack(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        time.sleep(5)
        home_page.sing_up("14251103", "123456789$$","click()")
        home_page.click_sing_up()
