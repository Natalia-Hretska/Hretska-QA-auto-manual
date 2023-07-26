import pytest

from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.mark.ui 
def test_check_incorrect_username():
    #Створення об'єкту для керування браузером
    driver = webdriver.Chrome(
        service = Service('C:/Users/grets/Hretska-QA-auto-manual/chromedriver-win64/chromedriver-win64/chromedriver.exe')
    )

    # відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    # Знаходимо поле, в яке будемо вводити неправильне імя користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    # Вводимо неправильні імя користувача або поштову адресу
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")      
    
    #  Знаходимо поле, в яке будемо вводити неправильний пароль 
    pass_elem = driver.find_element(By.ID, "password")
    
    #  Вводимо неправильний пароль
    pass_elem.send_keys("wrong password")
    
    #Знаходимо кнопку sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    # Емулюємо клік лівою кнопкою мишки
    btn_elem.click()
   
   # Перевіряємо, що назва сторінки така, яку ми очікували
    assert driver.title == 'Sign in to GitHub · GitHub'  
    
    #Закриваємо браузер
    driver.close()