from selenium import webdriver
import time
import math


browser = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = browser.get('http://suninjuly.github.io/alert_accept.html')

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(str(y))

    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(5)
    browser.quit()
