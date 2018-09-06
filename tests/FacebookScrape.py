
from selenium import webdriver

#we need to set chrome webdriver
chromedriver = '/Users/ryanyang/Desktop/InstaPy/assets/chromedriver'
driver = webdriver.Chrome(chromedriver)

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

from selenium.webdriver.common.keys import Keys
import time
from time import sleep

usr = ""
pwd = ""

# or you can use Chrome(executable_path="/usr/bin/chromedriver")
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)


driver.get('https://www.facebook.com/pg/vesselbags/reviews/?ref=page_internal')


SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    
names = driver.find_elements_by_xpath('//div[@class="_5pbx userContent _3576"]')

# writes to CSV
import csv


for i in range(len(names)):
    subArray = []
    print ( names[i].text + '\n')
    names[i].text.replace('\"', "")
    names[i].text.replace('\"', "")
    names[i].text.replace('\"', "")
    subArray.append(names[i].text)
    with open('out.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(subArray)
    


csvFile.close()

driver.close()


