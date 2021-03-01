from selenium import webdriver
import time, math
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    #element.send_keys(file_path)
    
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    
    answer = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)
    
    check = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check)
    check.click()
    
    radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    
    submit = browser.find_element_by_css_selector(".btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()