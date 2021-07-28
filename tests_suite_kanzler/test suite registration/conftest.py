import pytest
import time
from selenium import webdriver

@pytest.fixture
def open_website(request):
    link = 'https://kanzler:eK8ahoom@front.kanzler.garpix.com/ru'
    web = webdriver.Chrome(executable_path='/home/kanzler228/Documents/chromedriver')
    web.implicitly_wait(5)
    web.get(link)
def expand_shadow_element(element):
    web = webdriver.Chrome(executable_path='/home/kanzler228/Documents/chromedriver')
    shadow_root = web.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root