from selenium import webdriver
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    
    button = browser.find_element_by_css_selector(".btn")
    button.click()
    
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    button = browser.find_element_by_css_selector(".btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()