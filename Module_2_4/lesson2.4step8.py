import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = browser.get('http://suninjuly.github.io/explicit_wait2.html')

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element_by_id('book').click()

    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(str(y))
    browser.find_element_by_css_selector('#solve').click()

finally:
    time.sleep(30)
    browser.quit()
