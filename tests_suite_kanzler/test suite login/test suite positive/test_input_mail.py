import pytest
from selenium import webdriver
import time
import random
import string
def test_one_positive():
  #Генерация случайного мейла
  def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))
  web = webdriver.Chrome(executable_path='/home/kanzler228/Documents/chromedriver')
  #Генерация случайного номера телефона
  nu = ''
  for i in range(1, 10):
    nu+=str(i)
    nu = '7'+''.join(random.sample(nu,len(nu)))
  # выполняем тестовый сценарий 
  link = 'https://kanzler:eK8ahoom@front.kanzler.garpix.com/ru'
  #функция для нахождения корня
  def expand_shadow_element(element):
    shadow_root = web.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root
  #Открыть браузер  
  web.get(link)
  #Находим кнопку "Войти"
  input1 = web.find_element_by_xpath("//div[@class='index-module__header_middle_buttons__link___11FG4']")
  input1.click()
  time.sleep(1)
  #Прописываем теневые корни для нахождения необходимых форм
  root1 = web.find_element_by_xpath("//gx-input[@name='email']") #Форма "mail"
  shadow_root1 = expand_shadow_element(root1)
  root2 = web.find_element_by_xpath("//gx-input[@name='password']") #Форма "password"
  shadow_root2 = expand_shadow_element(root2)
  root3 = web.find_element_by_xpath("//gx-button[@type='submit']") #Форма "password"
  shadow_root3 = expand_shadow_element(root3)
  #Вводим мейл
  input1 = shadow_root1.find_element_by_name("email")
  input1.send_keys("bfxVRys@gmail.com")
  # Вводим пароль
  input2 = shadow_root2.find_element_by_name("password")
  input2.send_keys('Qd12345678')
  # Проверяем, действительно ли появилась надпись Об ошибке"
  #assert 'Имена должны содержать символы.' == find_text, 'Поле не найдено!' # 'Поле не найдено!' срабатывает, если в find_text пусто
  web.quit()
