from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time, math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = int(browser.find_element_by_id("num1").text)
    x2 = int(browser.find_element_by_id("num2").text)
    y = x1 + x2
    
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(y))
    
    submit = browser.find_element_by_css_selector(".btn")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()