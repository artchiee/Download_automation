from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from files import Files
import time
import re
from selenium.webdriver.common.action_chains import ActionChains
# site's url
global url
url = "https://feel.egybest.cz/"
driver = webdriver.Chrome("C:\\Users\\footb\\Downloads\\chromedriver")
# used to click on empty spaces to check if ads will show
body = driver.find_element_by_tag_name('body')

driver.get(url)
driver.implicitly_wait(6)


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
            driver.implicitly_wait(2)
            top_tag = driver.find_element_by_id("head")
            form = top_tag.find_element_by_tag_name('form')
            search_bar = form.find_element_by_class_name('autoComplete')
            # movies for now only
            search_for = input(
                str('What you want to search for today ? :  \n Search for movies only : '))
            search_bar.send_keys(search_for)
            driver.implicitly_wait(2)
            dropdown_search = form.find_element_by_tag_name('div')
            items = dropdown_search.find_elements_by_tag_name('a')
            all_movies = []
            movies_links = []
            for item in items:  
                text  = item.text
                link = item.get_attribute('href')
                movies_links.append(link)
                # only return real results not explore more
                find = re.compile(''movie)
                match  = list(filter(find.search, movies_links))
                all_movies.append(text)
            print('Movies urls are  : ', all_movies)

            # get all items from dropdown search bar
            #search_year = input(int('Enter movie by year : '))
            # element.send_keys(search_for)
            # element.send_keys(Keys.ENTER)

            # match user search againt site drop down search

            #print('your search was about this  :', search_for)

        else:
            print('noo ads shown !!!! ')
            pass

    except:
        Exception()


download_files()
