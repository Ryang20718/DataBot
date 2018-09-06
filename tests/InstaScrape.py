from selenium import webdriver
from selenium.webdriver.common.by import By

#we need to set chrome webdriver
chromedriver = '/Users/ryanyang/Desktop/InstaPy/assets/chromedriver'

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
driver.get('https://www.instagram.com/p/BmcQdtKg8AV/?taken-by=vesselbags')

# names = driver.find_elements_by_xpath('//li[@class="gElp9 "]/div[@class="C4VMK"]/span')
names = driver.find_elements_by_xpath('//div[@class="C4VMK"]/span')
owner = driver.find_elements_by_xpath('//div[@class="C4VMK"]/a[@class="FPmhX notranslate TlrDj"]')


def remove_non_ascii_1(text):

    return ''.join([i if ord(i) < 128 else '' for i in text])

# writes to CSV
import csv
for i in range(len(names)):
    comment = remove_non_ascii_1(names[i].text)
    subArray = []
    if comment != "" and owner[i].text != 'vesselbags':
        subArray.append(comment)
        with open('instagram.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(subArray)

csvFile.close()

driver.close()
