import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()
