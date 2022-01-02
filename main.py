'''
Beautiful Soup(bs4) is a Python library for pulling data out of HTML and XML files. This module does not come built-in with Python.

Request allows you to send HTTP/1.1 requests extremely easily. This module also does not come built-in with Python.

Selenium is one of the most popular automation testing tools. It can be used to automate browsers like Chrome, Firefox, Safari, etc.

Consider using Twilio free account for text messaging.
'''

import time
from selenium import webdriver
from datetime import datetime

# path of the chromedriver we have just downloaded
PATH = r"/applications/chromedriver"
driver = webdriver.Chrome(PATH)  # to open the browser

# url of google news website
url = 'https://reiwa.com.au/rental-properties/north-perth+leederville+wembley+highgate+joondanna+west-leederville+menora+mount-lawley+mount-hawthorn/houses+duplex+villas+townhouses+units/?2-2-beds+max-rental-price-425'

# to open the url in the browser
driver.get(url)

while (True):
    now = datetime.now()

    # this is just to get the time at the time of
    # web scraping
    current_time = now.strftime("%H:%M:%S")
    print(f'At time : {current_time} ')

    # Used f-strings to format the string
    c = 1
    for x in range(1, 10):
        house_path = ''
        # Exception handling to handle unexpected changes
        # in the structure of the website
        try:
            house_path = f'//*[@id="item-{x}"]'
            # to get that element
            house = driver.find_element_by_xpath(house_path)
        except:
            continue
        print(f"House {c}: ")
        c += 1

        # to read the text from that element
        print(house.text)
        print()

    # to stop the running of code for 30 mins
    time.sleep(1200)





