import pytest
from selenium import webdriver
from constants import Constants


@pytest.fixture(params=["firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()
    browser.get(Constants.URL)
    yield browser
    browser.quit()