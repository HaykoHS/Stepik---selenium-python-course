from selenium import webdriver
import time
import math

browser = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    treasure = browser.find_element_by_id('treasure')
    treasure_attribute = treasure.get_attribute('valuex')
    print('value of the chest', treasure_attribute)
    assert treasure_attribute is not None, 'Value under treasure icon is not reachable'

    x = treasure_attribute
    y = calc(x)

    browser.find_element_by_css_selector('#answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()

    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(10)
    browser.quit()
