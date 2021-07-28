import pytest
from selenium import webdriver
import time
import random
import string
def test_three():
  #Генерация случайного мейла
  def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))
  web = webdriver.Chrome(executable_path='/home/kanzler228/Documents/chromedriver')
  #Генерация случайного номера телефона
  nu = ''
  for i in range(1, 10):
    nu+=str(i)
    nu = '7'+''.join(random.sample(nu,len(nu)))
  #функция для нахождения корня
  def expand_shadow_element(element):
    shadow_root = web.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root


  # выполняем тестовый сценарий 
  link = 'https://kanzler:eK8ahoom@front.kanzler.garpix.com/ru'
  #функция для нахождения корня

  def expand_shadow_element(element):
    shadow_root = web.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root
  #Открыть браузер  
  web.get(link)
  web.implicitly_wait(5)
  #Находим кнопку "Войти"
  input1 = web.find_element_by_xpath("//div[@class='index-module__header_middle_buttons__link___11FG4']")
  input1.click()
  #Прописываем теневые корни для нахождения необходимых форм
  root1 = web.find_element_by_xpath("//gx-input[@name='email']") #Форма "mail"
  shadow_root1 = expand_shadow_element(root1)
  root2 = web.find_element_by_xpath("//gx-input[@name='password']") #Форма "password"
  shadow_root2 = expand_shadow_element(root2)
  root3 = web.find_element_by_xpath("//gx-button[@type='submit']") #Форма "password"
  shadow_root3 = expand_shadow_element(root3)
  time.sleep(1)
  #Вводим мейл
  input1 = shadow_root1.find_element_by_name("email")
  input1.send_keys(random_char(7)+"@gmail.com")

  # Нажимаем кнопку "Войти"
  time.sleep(5)
  input3 = web.find_element_by_xpath("//gx-button[@type='submit']")
  webdriver.ActionChains(web).move_to_element(input3 ).click(input3 ).perform()
  input3.click()
  x = web.find_element_by_xpath("//div[@class='index-module__error___JxOWR']")
  find_text= x.text
  print(find_text)
  assert 'Некорректные данные для аутентификации!'== find_text, 'Строка не найдена'
  time.sleep(3)
  web.quit()



