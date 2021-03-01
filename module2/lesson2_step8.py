from selenium import webdriver
import time, math
import os 
  
try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    
    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("N")
    
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("N")
    
    email = browser.find_element_by_name("email")
    email.send_keys("N")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    
    file = browser.find_element_by_id("file")
    file.send_keys(file_path)
    
    submit = browser.find_element_by_css_selector(".btn")
    submit.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()