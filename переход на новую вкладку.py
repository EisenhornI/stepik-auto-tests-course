from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("trollface")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    submit = browser.find_element_by_class_name("btn")
    submit.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
