import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from files import Files
import time
import re
from selenium.webdriver.common.action_chains import ActionChains

import lxml.html as lh
import json

global site_url
# site_url = "https://epco.egybest.com/movie/abduction-2011/"

down_btn = 'https://epco.egybest.com/movie/split-2017/?ref=search-p1'
driver = webdriver.Chrome("C:\\Users\\nouamane\\Downloads\\chromedriver")


def scrapp_dt():
    # scroll = ActionChains(driver)
    # table_tg = driver.find_element_by_xpath('//*[@id="watch_dl"]/table')
    # scroll.move_to_element(table_tg).perform()
    # driver.implicitly_wait(3)

    # Create a handle, page, to handle the contents of the website
    page = requests.get(down_btn)
    print('page : ', page)
    # site = []
    current_page = down_btn
    r = requests.get(current_page)
    print('selen:', r)

    # site.append(str(current_page))
    # new = site
    # print('url :  ', new)
    # time.sleep(2)
    # #Store the contents of the website under doc
    # doc = lh.fromstring(r.content)
    # #Parse data that are stored between <tr>..</tr> of HTML
    # table_tg = driver.find_element_by_xpath(
    # '//*[@id="watch_dl"]/table')
    # size_quality = doc.xpath('//table/tbody/tr/td[3]')

    # Will print all quality/size available for any movie
    # quality = []
    # size = []
    # for i in tr_quality:
    #     for x in size_quality:
    #         n_qualities = i.text_content()
    #         s_quality = x.text_content()
    #         #print ('%d: ' "%s" %(counter,all_sizes
    #         quality.append(n_qualities)
    #         size.append(s_quality)
    # print('number  : ', quality,'\n''size', size )

    # get link quality from user input

    # quality_choice = input(str('Type quality Number only  :  '))
    # pattern = re.compile(r'\d*'  + str(quality_choice), re.I)
    # result = list(filter(pattern.search, quality))
    # if result:
    #     print('Found match :', result)
    # else:
    #     print('exception')

  name = driver.find_element_by_xpath('//*[@id="mainLoad"]/div[1]/div/h1').text
  if name:
      print('name ' : name)


scrapp_dt()
