import time
from selenium import webdriver

browser = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')
time.sleep(2)
browser.execute_script("document.title='Script executing';alert('Robots at work');")
