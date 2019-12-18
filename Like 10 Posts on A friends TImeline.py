import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome('/home/sangwan/Softwares_Installed/chromedriver_linux644/chromedriver',options=chrome_options)

driver.get('https://www.facebook.com/')
driver.maximize_window()

						#LOGIN STARTS

username = input("Enter Email:- ")
password = input("Enter password:- ")

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
					# LOGIN DONE 

# My TimeLine
my_timeline = driver.find_element_by_class_name('_1vp5')
my_timeline.click()

# Friends Button
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='_6-6']"))).click() #Works Fine

#Moving to Friends List ELEMENT
ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,'pagelet_timeline_medley_friends')))).perform()

# First See All Button
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='_3t5 fwb']"))).click()

#Scrolling From Top to Bottom of the Friends List:-
# Range Might be Change According to your no. of Friends
for i in range(15): #iterating 15 times BUT will not exceed the Friend's List

	driver.execute_script("document.getElementById('pagelet_timeline_medley_friends').scrollIntoView(false)")
	time.sleep(1)
	print("Scrolling in Friends List:- {}".format(i))

target_friend_name = input("Enter Name of Target Friend:-")
friend = driver.find_element_by_link_text(target_friend_name)

#Moving to the Target Friend Link.
ActionChains(driver).move_to_element(friend).perform()
time.sleep(3)
friend.click()

#Scrolling Around the Friend's TimeLine
elem = driver.find_element_by_tag_name("body")
no_of_pagedowns = 25
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1
print("Page down Complete")

#Performing Likes:)
exps = 0
for i in range(10):
	try:
		like = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//a[@class=' _6a-y _3l2t  _18vj']")))
		ActionChains(driver).move_to_element(like).click(like).perform()
		print('{} Liked'.format(i+1))
	except:
		driver.find_element_by_tag_name('html').send_keys(Keys.END)
		print("This Like will not be counted as an Exception just Occured.")
		exps = exps+1
print("YOU HAVE LIKED TOP {} POSTS ON {}'s TIMELINE...".format(10-exps,target_friend_name))

