from selenium import webdriver
import time

try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/wait1.html"
    browser.get(link)
    
    time.sleep(1)
    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()