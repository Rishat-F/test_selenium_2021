from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


def test_search_something():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    try:
        driver.get("https://www.google.com/")
        search_input = driver.find_element_by_name("q")
        search_input.clear()
        search_input.send_keys("python")
        search_input.send_keys(Keys.ENTER)
        assert "python" in driver.page_source
    finally:
        driver.quit()


def test_search_nothing():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    try:
        driver.get("https://www.google.com/")
        search_input = driver.find_element_by_name("q")
        search_input.clear()
        search_input.send_keys("")
        search_input.send_keys(Keys.ENTER)
        assert driver.current_url == "https://www.google.com/"
    finally:
        driver.quit()


test_search_something()
test_search_nothing()
