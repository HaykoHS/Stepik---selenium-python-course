from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    for element in elements:
        element.send_keys("some")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    # browser.quit()

# не забываем оставить пустую строку в конце файла
