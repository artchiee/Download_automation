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

global url
# site_url = "https://epco.egybest.com/movie/abduction-2011/"

url = ' https://epco.egybest.com/movie/split-2017/'
driver = webdriver.Chrome("C:\\Users\\nouamane\\Downloads\\chromedriver")


def scrapp_dt():
    # scroll = ActionChains(driver)
    # table_tg = driver.find_element_by_xpath('//*[@id="watch_dl"]/table')
    # scroll.move_to_element(table_tg).perform()
    # driver.implicitly_wait(3)

    # Create a handle, page, to handle the contents of the website
    page = requests.get(url)
    print('page : ', page)
    # site = []
    current_page = url
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

    data = []
     table_loop = driver.find_element_by_xpath('//*[@id="mainLoad"]/div[2]/div[2]/table')
            tbody_loop = table_loop.find_element_by_tag_name('tbody')
           # tr_loop = tbody_loop.find_elements_by_tag_name('tr')

            #for i in tbody_loop.find_elements_by_tag_name('tr[%d]'%counter):

            # information to save as json data objs
            should_add = True
            name = ''
            duration_time = ''
            year = ''
            quality_type = '' # (full hd or hd etc)
            quality_size = '' #(by gb|mb)
            url = ''
            stars = ''
            try:
                name = tbody_loop.find_elements_by_xpath('//tr[1]/td/h1').text
                duration_time  = tbody_loop.find_elements_by_xpath('//tr[6]/td[2]').text
                year = '2000'
                stars = tbody_loop.find_elements_by_xpath('//tr[5]/td[2]/strong/span').text
                #append data to list
                all_data.append(name)
                print('ALL DATA : ', all_data)
            except:
                print('exception in saving/getting data')


scrapp_dt()
