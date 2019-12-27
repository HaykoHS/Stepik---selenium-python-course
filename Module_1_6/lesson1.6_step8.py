from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input[name="first_name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")

    buttons = browser.find_elements(By.XPATH, '//button[@type="submit"]')
    for button in buttons:
        button.click()

finally:
    time.sleep(30)
    browser.quit()
