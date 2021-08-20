from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


BASE_URL = "https://www.google.com/"


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(BASE_URL)

    def get_page_source(self):
        return self.driver.page_source

    @property
    def current_url(self):
        return self.driver.current_url

    def find_element(self, locator, wait_time=5):
        wait = WebDriverWait(self.driver, wait_time)
        element = wait.until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )
        return element

    def search_input(self, locator):
        search_input = self.find_element(locator)
        return search_input

    def fill(self, element, text):
        element.clear()
        element.send_keys(text)
        return element

    def search_enter(self, search_input):
        search_input.send_keys(Keys.RETURN)
        return self

    def quit(self):
        self.driver.quit()
