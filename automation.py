from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_browser = webdriver.Chrome('chromedriver')


#chrome_browser.maximize_window()
chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

assert "Selenium Easy Demo" in chrome_browser.title

show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
assert 'Show Message' in chrome_browser.page_source

input_enter_message = chrome_browser.find_element(By.ID, 'user-message')
input_enter_message.clear()
input_enter_message.send_keys("I am...")
show_message_button.click()
output_message = chrome_browser.find_element(By.ID, 'display')
assert "I am..." in output_message.text

chrome_browser.close()

while True:
    pass