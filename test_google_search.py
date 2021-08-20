from pages.main_page import MainPage


def test_search_something(browser):
    main_page = MainPage(browser)
    main_page.open_page()
    main_page.search("python")
    assert "python" in main_page.get_page_source()


def test_search_nothing(browser):
    main_page = MainPage(browser)
    main_page.open_page()
    main_page.search("")
    assert "https://www.google.com/" == main_page.current_url
