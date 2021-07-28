#НЕОБХОДИМ ТЕСТ РАБОТОСПОСОБНОСТИ 
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import random
import string
def test_three():
  #Генерация случайного мейла
  def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))
  web = webdriver.Chrome(executable_path='/home/kanzler228/Documents/chromedriver')
  #Генерация случайного номера телефона
  nu = ''
  for i in range(1, 11):
    nu+=str(i)
    nu = ''.join(random.sample(nu,len(nu)))
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
  #Находим кнопку "Зарегистрироваться"
  input2 = web.find_element_by_xpath("//gx-button[@class='index-module__button--white___3jkn4 hydrated']")
  input2.click()
  #Прописываем теневые корни для нахождения необходимых форм
  root1 = web.find_element_by_xpath("//gx-input[@name='first_name']") #Форма "Имя"
  shadow_root1 = expand_shadow_element(root1)
  root2 = web.find_element_by_xpath("//gx-input[@name='last_name']") #Форма "Фамилия"
  shadow_root2 = expand_shadow_element(root2)
  root3 = web.find_element_by_xpath("//gx-input[@name='middle_name']") #Форма "Отчество"
  shadow_root3 = expand_shadow_element(root3)
  root4 = web.find_element_by_xpath("//gx-input[@name='city']") #Форма "Город"
  shadow_root4 = expand_shadow_element(root4)
  root5 = web.find_element_by_xpath("//gx-input[@name='email']") #Форма "Почта"
  shadow_root5 = expand_shadow_element(root5)
  root6 = web.find_element_by_xpath("//gx-phone-input[@name='phone']") #Форма "Телефон"
  shadow_root6 = expand_shadow_element(root6)
  root7 = web.find_element_by_xpath("//gx-input[@name='birthday']") #Форма "Дата рождения"
  shadow_root7 = expand_shadow_element(root7)
  root8 = web.find_element_by_xpath("//gx-input[@name='height']") #Форма "Рост"
  shadow_root8 = expand_shadow_element(root8)
  root9 = web.find_element_by_xpath("//gx-input[@name='weight']") #Форма "Вес"
  shadow_root9 = expand_shadow_element(root9)
  root10 = web.find_element_by_xpath("//gx-input[@name='password']") #Форма "Пароль"
  shadow_root10 = expand_shadow_element(root10)
  root11 = web.find_element_by_xpath("//gx-input[@name='again_password']") #Форма "Подтвердить пароль"
  shadow_root11 = expand_shadow_element(root11)
  root12 = web.find_element_by_xpath("//gx-button[@class='index-module__button--black___oERDx hydrated']") #Кнопка "Зарегистр"
  shadow_root12 = expand_shadow_element(root12)
  # Заполнение формы "Имя"
  string1 = shadow_root1.find_element_by_name('first_name')
  string1.send_keys('Ваня')
  # Заполнение формы "Фамилия"
  string2 = shadow_root2.find_element_by_name('last_name')
  string2.send_keys('Иванов')
  # Заполнение формы "Отчество"
  string3 = shadow_root3.find_element_by_name('middle_name')
  string3.send_keys('Иванович')
  # Заплнение формы "Мейл"
  string5 = shadow_root5.find_element_by_name('email')
  string5.send_keys(random_char(7)+"@gmail.com")
  time.sleep(2)
  # Заполнение формы "Телефон"
  string6 = shadow_root6.find_element_by_class_name("form-control")
  string6.send_keys(nu)
  time.sleep(5)
  # Заполнение формы "День рождения"
  string7 = shadow_root7.find_element_by_name("birthday")
  string7.send_keys('12121111')
  # Заполнение формы "Рост"
  string8 = shadow_root8.find_element_by_name("height")
  string8.send_keys('100')
  # Заполнение формы "Вес"
  string9 = shadow_root9.find_element_by_name("weight")
  string9.send_keys('50')
  # Заолнение формы "Пароль"
  string10 = shadow_root10.find_element_by_name("password")
  string10.send_keys('N1m@mail.ru')
  # Заполнение формы "Подтверждение пароля"
  string11 = shadow_root11.find_element_by_name("again_password")
  string11.send_keys('N1m@mail.ru')
  # Клик по кнопке "Зарегистрироваться"
  string12 = web.find_element_by_xpath("//gx-button[@type='submit']")
  time.sleep(3)
  string12.click()
  time.sleep(3)
  # Ищем надпись "Обязательное поле!"
  er = web.find_element_by_xpath("//gx-input[@name='city']/div[@slot='help-text']")
  # Скролим окно до момента появления надписи "Обязательное поле!"
  web.execute_script("return arguments[0].scrollIntoView(true);", er)
  # Создаем переменную и записываем туда нашу надпись, переводим в текстовый формат
  find_text = er.text
  time.sleep(5)
  # Проверяем, действительно ли появилась надпись "Обязательное поле!"
  #assert 'Обязательное поле!' == find_text, 'Поле не найдено!' # 'Поле не найдено!' срабатывает, если в find_text пусто
  #ПОЛЯ БЫТЬ НЕ ДОЛЖНО!
  web.quit() 
