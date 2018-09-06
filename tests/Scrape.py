
from selenium import webdriver

#we need to set chrome webdriver
chromedriver = '/Users/ryanyang/Desktop/InstaPy/assets/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get('https://www.facebook.com/pg/vesselbags/reviews/?ref=page_internal')


SCROLL_PAUSE_TIME = 0.5

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

for i in range(len(names)):
    print ( names[i].text + '\n')
driver.close()


