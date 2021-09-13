from selenium import webdriver
import pytest


def pytest_adoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: es or ru")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
