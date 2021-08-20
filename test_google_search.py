from app import Application


def test_search_something():
    app = Application()
    try:
        app.main_page.open_page()
        app.main_page.search("python")
        assert "python" in app.main_page.get_page_source()
    finally:
        app.main_page.quit()


def test_search_nothing():
    app = Application()
    try:
        app.main_page.open_page()
        app.main_page.search("")
        assert "https://www.google.com/" == app.main_page.current_url
    finally:
        app.main_page.quit()


test_search_something()
test_search_nothing()
