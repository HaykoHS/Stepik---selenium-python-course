import time
import math
from selenium import webdriver

browser = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = browser.get('http://suninjuly.github.io/execute_script.html')

    find_x_id = browser.find_element_by_id('input_value')
    x = find_x_id.text
    y = calc(x)
    print(y)
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("window.scrollBy(0, 110);")

    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()

    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(10)
    browser.close()
