from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"


browser = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')
browser.get(link)

time.sleep(3)
found_link = str(math.ceil(math.pow(math.pi, math.e)*10000))
browser.find_element_by_link_text(found_link).click()

input1 = browser.find_element_by_tag_name('input[name="first_name"]')
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name('city')
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id('country')
input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()


# browser.quit()