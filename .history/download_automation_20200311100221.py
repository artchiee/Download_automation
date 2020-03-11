import json
import requests
from bs4 import BeautifulSoup
from files import Details
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
from selenium.webdriver.common.action_chains import ActionChains
import lxml.html as lh

# handling time out exceptions
from selenium.common.exceptions import TimeoutException

# site's url
global site_url
site_url = "https://epco.egybest.com/"
driver = webdriver.Chrome("C:\\Users\\nouamane\\Downloads\\chromedriver")
driver.get(site_url)
time.sleep(6)


def download_files():
    # ignore the notification message if shown
    action = ActionChains(driver)
    message_box = driver.find_element_by_id('NotificationsAskMsg')
    action.move_to_element(message_box).perform()
    inside_msg = driver.find_element_by_tag_name('p')
    action.move_to_element(inside_msg).perform()
    dismiss = driver.find_element_by_class_name('NotificationIgnore')
    action.move_to_element(dismiss).perform()
    dismiss.click()

    # Ads handling here
    window_before = driver.window_handles[0]
    try:
        window_after = driver.window_handles[1]
        if window_after:
            driver.switch_to.window(window_after)
            driver.implicitly_wait(3)
            driver.close()
            # back to original window
            driver.switch_to.window(window_before)
            driver.implicitly_wait(4)

            # Getting user movie choice
            search_for = input(
                str('What you want to search for today ? :  \n Search for movies only : '))
            try:
                # Search bar field
                top_tag = driver.find_element_by_id("head")
                form = top_tag.find_element_by_tag_name('form')
                search_bar = form.find_element_by_class_name('autoComplete')
                search_bar.send_keys(search_for)
                driver.implicitly_wait(5)

                dropdown_search = form.find_element_by_tag_name('div')
                items = dropdown_search.find_elements_by_tag_name('a')
                all_movies = []  # for movie title
                movies_links = []  # movie links
                for item in items:
                    text = item.text
                    all_movies.append(text)
                    link = item.get_attribute('href')
                    movies_links.append(link)
                print('Available Movies for this Search are : ', all_movies)
            except TimeoutException as ex:
                print('Time out Exception' + str(ex))

            # Getting user movie year
            movie_year = input(str('On what Year : '))

            # return matched title and link typed by user
            # need to match any title pattern
            match_title = re.compile(
                search_for + r'\s+\?|\w+\?|\W+.*?' + '\(%s\)+' % str(movie_year), re.I)
            title_rs = list(filter(match_title.search, all_movies))

            link_match = re.compile(
                '/(movie|serie)/' + search_for + r'\s+\?|\w+\?|\W+.*?' + movie_year, re.I)
            link_rs = list(filter(link_match.search, movies_links))

            if title_rs and link_rs:
                print('Found Title match : ', title_rs,
                      '\n', 'Full movie url : ',  link_rs, '\n')
            else:
                print('Nothing Found ')

            # get next url --> next page
            mid_url = re.compile(r'/(movie|serie)/.+')
            url_match = [mid_url.search(var).group()
                         for var in link_rs if mid_url.search(var)]
            if url_match:
                print('mid url taken is : ', url_match ,'\n')
                convertion = ''.join(link_rs)
                # Enter the requested url
                driver.implicitly_wait(2)
                driver.get(convertion)
            else:
                print('exception')

            driver.implicitly_wait(10)
            all_data = []
            counter = 0
            # will initiate a for loop here
            table_loop = driver.find_element_by_xpath('//*[@id="mainLoad"]/div[2]/div[2]/table')
            tbody_loop = table_loop.find_element_by_tag_name('tbody')
           # tr_loop = tbody_loop.find_elements_by_tag_name('tr')

            #for i in tbody_loop.find_elements_by_tag_name('tr[%d]'%counter):

            # information to save as json data objs
            should_add = True
            duration_time = ''
            stars = ''
            try:
                duration_time  = tbody_loop.find_elements_by_xpath('//tr[6]/td[2]').text
                stars = tbody_loop.find_elements_by_xpath('//tr[5]/td[2]/strong/span').text
            except:
                Exception()
                should_add = False
                
            print('*****',*8)

            # Next : is to select quality and download
            # Before the page scroll it will wiat 6s to fully load
            driver.implicitly_wait(6)
            scroll = ActionChains(driver)
            table_tg = driver.find_element_by_xpath(
                '//*[@id="watch_dl"]/table')
            scroll.move_to_element(table_tg).perform()
            driver.implicitly_wait(3)
            current_page = driver.current_url

            # print('running url is : ',str(current_page) , '\n')
            time.sleep(3)
            response = requests.get(current_page)
            # print('selenium response :', response )
            doc = lh.fromstring(response.content)
            quality_values = doc.xpath('//table/tbody/tr/td[2]')
            # quality_size to store as json
           # quality_number  = doc.xpath('//table/tbody/tr/td[3]')

            qualities = []
            for all_qualities in quality_values:
                data = all_qualities.text_content()
                qualities.append(data)
            print('Qualities found : ', qualities)

            # Match quality user input against quality_list[]
            quality_choice = input(
                str('Type quality Number (1080 | 720)  only --> (without :p or    hd ..) :  '))
            pattern = re.compile(r'\d*' + str(quality_choice), re.I)
            result = list(filter(pattern.search, qualities))
            if result:
                print('Found match :', result)

                # This allow users to select either full-hd quakity or HD
                if quality_choice == '1080':
                    download_btn = table_tg.find_element_by_xpath(
                        'tbody/tr[1]/td[4]')
                    a_tag = download_btn.find_element_by_tag_name('a')
                    btn_link = a_tag.get_attribute('data-url')
                elif quality_choice == '720':
                    download_btn = table_tg.find_element_by_xpath(
                        'tbody/tr[2]/td[4]')
                    a_tag = download_btn.find_element_by_tag_name('a')
                    btn_link = a_tag.get_attribute('data-url')
                else:
                    print('Only 1080 or 720 allowed')
                    # if True:
                if btn_link:
                    # Will handle the ad just to make sure everything goes well
                    try:
                        print('Found url : ', btn_link)
                        driver.implicitly_wait(3)
                        a_tag.click()
                    except window_after:
                        driver.switch_to_window(window_after)
                        driver.implicitly_wait(2)
                        driver.close()
                        driver.switch_to_window(window_before)
                        time.sleep(2)
                        # Click btn download
                        a_tag.click()
                else:
                    print('exception')

            else:
                print('exception --> Invalid Quality input !! ')

            # later will add automatic button download

        else:
            print('noo ads shown !!!! ')
            pass
    except KeyboardInterrupt:
        print('Keybord Interruption')

    counter = 0

    name = ""
    year = ''
    quality_type = ""
    quality_size = ""
    url = ""

    print('Json Data has been created\n')
    # Saving data into json file to access later 
    final_data = [] #will store the data got from each element
    try:
        name = search_for
        year  = movie_year
        quality_type = quality_choice
        quality_size = "1.6GB"

    except: 
        print('exception')
        should_add = False

    # save All my data (class)
    my_data = Details(name, year, duration_time, quality_type, quality_size, stars)
    if my_data:
        final_data.append(my_data)
    counter = counter + 1

    # Writing my data into a simple text file
    #import csv
    with open('information.json', 'w') as json_file:
        data = {}
        data["Files"] = []
        for f_data in final_data:
            data["Files"].append(f_data.serialize())
        json.dump(data, json_file, sort_keys=True, indent=4)

    print(json.dumps(name.serialize(), indent=4, sort_keys=True))
    print(json.dumps(year.serialize(), indent=4, sort_keys=True))

download_files()
