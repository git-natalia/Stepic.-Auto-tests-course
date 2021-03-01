from selenium import webdriver
import time, math

try: 
    browser = webdriver.Chrome()
 
    browser.execute_script("document.title='Script executing';alert('Robots at work');")


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()