import time
from selenium import webdriver

browser = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
time.sleep(1)
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
browser.execute_script("window.scrollBy(0, 105);")
button.click()
assert True


time.sleep(5)
browser.close()





#
# // javascript
# button = document.getElementsByTagName("button")[0];
# button.scrollIntoView();