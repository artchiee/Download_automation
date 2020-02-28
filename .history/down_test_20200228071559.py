import  requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from files import Files
import time
import re
from selenium.webdriver.common.action_chains import ActionChains

import lxml.html as lh
import  json

global site_url
#site_url = "https://epco.egybest.com/movie/abduction-2011/"

down_btn = 'https://vidstream.online/f/WR8M2fbSmc/?vclid=9ceb943042d9011bebf06b17f25c27c4704ed8374f42fd6937681639AgggAmBvfAgDgAvMHLIHCIAtbKaElUQpHDgADAgAtNzgAgDgAswzXERjvvAvQhLWgBAXUlAgM'
driver = webdriver.Chrome("C:\\Users\\nouamane\\Downloads\\chromedriver")

def scrapp_dt():
    # scroll = ActionChains(driver)
    # table_tg = driver.find_element_by_xpath('//*[@id="watch_dl"]/table')
    # scroll.move_to_element(table_tg).perform()
    # driver.implicitly_wait(3)
    
    #Create a handle, page, to handle the contents of the website
    # page = requests.get(site_url)
    # print('page : ', page)
    # site = []
    # current_page = site_url
    # r = requests.get(current_page)
    # print('selen:',r )  

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

    #get link quality from user input 

    # quality_choice = input(str('Type quality Number only  :  '))
    # pattern = re.compile(r'\d*'  + str(quality_choice), re.I)
    # result = list(filter(pattern.search, quality))
    # if result:
    #     print('Found match :', result)
    # else:
    #     print('exception')
    
    p_xpath = driver.find_element_by_xpath('/html/body/div[1]/div/p[2]')
    a_tag = p_xpath.find_element_by_class_name('bigbutton')
    i_tag = a_tag.find_element_by_tag_name('i')
    if i_tag:
        i_tag.click()
    else:
        print('element not clickable')

scrapp_dt()
