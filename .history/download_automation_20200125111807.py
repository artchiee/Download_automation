from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from files import Files
import time

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
message  = driver.find_element_by_id('NotificationsAskMsg')
if message:
    dissmiss = message.find_element_by_class_name('NotificationIgnore api')
    dissmiss.click()

element.send_keys(search_for)
element.send_keys(Keys.ENTER)
