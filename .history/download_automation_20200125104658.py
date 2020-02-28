from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from files import  Files
import time 

# site's url

global url  
url = "https://feel.egybest.cz/"
driver = webdriver.Chrome("C:\\Users\\footb\\Downloads\\chromedriver")

search_for = input(str('What you want to search for today ? :  \n'))
top_tag  = driver.find_element_by_xpath('//*[@id="head"]/div/div[2]/form')
element  = top_tag.find_element_by_class_name('q autoComplete')
driver.get(url)
element.send_keys(search_for)
element.send_keys(Keys.ENTER)


    
