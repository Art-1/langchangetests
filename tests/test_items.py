link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_btn(browser):
    browser.get(link)
    import time
    time.sleep(10)
    assert browser.find_element_by_css_selector(".btn-add-to-basket")
    assert True


""" Run: pytest -s -v --language=en --browser_name=chrome test_items.py """