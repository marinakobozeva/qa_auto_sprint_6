import pytest
from selenium import webdriver
from constants.constants_url import Constants_Url


@pytest.fixture(params=["firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()
    browser.get(Constants_Url.URL)
    yield browser
    browser.quit()