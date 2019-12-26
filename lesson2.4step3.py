from selenium import webdriver
import time

browser = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')
browser.implicitly_wait(5)

try:
    link = browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    time.sleep(3)
    browser.quit()
