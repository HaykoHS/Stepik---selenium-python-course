import os
import time
from selenium import webdriver


browser = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')

try:
    website = browser.get('http://suninjuly.github.io/file_input.html')

    fist_name = browser.find_element_by_css_selector('input[name="firstname"]')
    fist_name.send_keys("Incredible")
    last_name = browser.find_element_by_css_selector('input[name="lastname"]')
    last_name.send_keys('Me')
    email = browser.find_element_by_css_selector('input[name="email"]')
    email.send_keys('hs88695@yopmail.com')

    uploading_button = browser.find_element_by_id('file')
    uploading_button.send_keys('C:\Python files\incredibleme.txt')

    browser.find_element_by_css_selector('button.btn').click()


finally:
    time.sleep(10)
    browser.quit()
