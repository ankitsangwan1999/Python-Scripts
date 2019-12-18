'''
Requirements:
	selenium package
		pip install selenium
	ChromeDriver
		https://chromedriver.storage.googleapis.com/index.html?path=2.25/
	Chromium Web Browser( Open source version of chrome browser )
		sudo apt-get install chromium-browser

'''

import os
from selenium import webdriver


driver = webdriver.Chrome('/###ENTER_LOCAL_PATH##chromedriver_linux644/chromedriver')
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of the user: ')
msg = input('Enter the Message: ')
count = int(input('Enter the no. of times to send the Message: '))

input('Enter any key after scanning QR code: ')
user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_13mgZ')
	
for i in range(count):
	msg_box.send_keys(msg)
	button = driver.find_element_by_class_name('_3M-N-')
	button.click() 
print("Messages Sent Successfully.")
