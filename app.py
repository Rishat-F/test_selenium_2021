from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page import MainPage


class Application:
    def __init__(self, driver=webdriver.Chrome(ChromeDriverManager().install())):
        self.driver = driver
        self.main_page = MainPage(driver)

    def quit(self):
        self.driver.quit()
