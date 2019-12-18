import os
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome('/home/sangwan/Softwares_Installed/chromedriver_linux644/chromedriver',options=chrome_options)

driver.get('https://www.facebook.com/')

username = input("Enter Email: ")
password = input("Enter password: ")

username_field = driver.find_element_by_name('email')
password_field = driver.find_element_by_name('pass')

username_field.send_keys(username)
password_field.send_keys(password)

try:
	login_button = driver.find_element_by_id('loginbutton')
	login_button.click()
except:
	login_button = driver.find_element_by_name('login')
	login_button.click()

print("You have Logged in Successfully!")
