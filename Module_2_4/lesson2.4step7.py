import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")

browser.get("http://suninjuly.github.io/wait2.html")

button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'verify')))
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

time.sleep(2)
browser.quit()
