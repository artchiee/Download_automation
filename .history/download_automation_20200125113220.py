from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from files import Files
import time
from selenium.webdriver.common.action_chains import ActionChains
# site's url
global url
url = "https://feel.egybest.cz/"
driver = webdriver.Chrome("C:\\Users\\footb\\Downloads\\chromedriver")

# search_for = input(str('What you want to search for today ? :  \n'))
# top_tag  = driver.find_element_by_id("head")
# form   = top_tag.find_element_by_tag_name('form')
# element = form.find_element_by_class_name('q autoComplete')
driver.get(url)
driver.implicitly_wait(8)
# ignore the notification message if shown
action = ActionChains(driver)
message_box  = driver.find_element_by_id('NotificationsAskMsg')
action.move_to_element(message_box).perform() 
inside_msg   = driver.find_element_by_tag_name('p')
action.move_to_element(inside_msg).perform()
dismiss  = driver.find_element_by_class_name('NotificationIgnore')
action.move_to_element(dismiss).perform()
dismiss.click()
