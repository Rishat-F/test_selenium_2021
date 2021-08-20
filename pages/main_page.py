from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPageLocators:
    SEARCH_INPUT = (By.NAME, "q")


class MainPage(BasePage):

    def search(self, text):
        search_input = self.search_input(MainPageLocators.SEARCH_INPUT)
        search_input = self.fill(search_input, text)
        self.search_enter(search_input)
        return self
