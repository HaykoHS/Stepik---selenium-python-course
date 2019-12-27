import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')
try:
    link = browser.get('http://suninjuly.github.io/selects1.html')
    time.sleep(2)

    sel_number1 = browser.find_element_by_id('num1')
    sel_number1_value = int(sel_number1.text)
    print(sel_number1_value)

    sel_number2 = browser.find_element_by_id('num2')
    sel_number2_value = int(sel_number2.text)
    print(sel_number2_value)

    total_value = int(sel_number1_value) + int(sel_number2_value)
    print(total_value)

    b5 = Select(browser.find_element_by_id('dropdown'))
    b5.select_by_visible_text(str(total_value))

    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(10)
    browser.quit()
