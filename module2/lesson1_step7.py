from selenium import webdriver
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_image = browser.find_element_by_css_selector("img")
    x = x_image.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    
    check = browser.find_element_by_id("robotCheckbox")
    check.click()
    
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    
    submit = browser.find_element_by_css_selector(".btn")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()