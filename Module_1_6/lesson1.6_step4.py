from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"


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
button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(30)
browser.quit()

# не забываем оставить пустую строку в конце файла
