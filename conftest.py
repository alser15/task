import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome")
    parser.addoption('--language', action='store', default=None,
                     help='Choose language: en')                 


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options, executable_path='/home/kanzler228/Documents/chromedriver')
    elif user_language == 'ru':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options, executable_path='/home/kanzler228/Documents/chromedriver')
        
    else:
        raise pytest.UsageError("--error--")
    yield browser
    print("\nquit browser..")
    time.sleep(3)
    browser.quit()