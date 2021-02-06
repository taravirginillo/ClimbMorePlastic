 # GroundUp Automated Booking Script
 # Owner : Anonymous
 # Last Update : February 6th, 2021
 # 
 # Selenium docs for reference : https://selenium-python.readthedocs.io/locating-elements.html
 
from selenium import webdriver

# Connect to chromedriver & load website
url = "https://app.rockgympro.com/b/widget/?a=offering&offering_guid=fd63ba3934f44647a1151b4ef6507d77&widget_guid=e8cacb9641fa4f6ea12a176adc3a3570&random=601c56694c33c&iframeid=rgpiframe601c43cdd5d13&mode=e&course_guid=ca4ec882966b50e97b44e1832333108e6169537b"
driver = webdriver.Chrome(executable_path=r'C:/Program Files/Chromedriver/chromedriver.exe')
driver.get(url)

# ----------------------------------Global Variables --------------------------------------------------------------------
# Script not set to accept 2 participants (yet)
PARTICIPANT_NUM = 1
WEEK_OF_MONTH = 2
DAY_OF_WEEK = 4 # Sunday = 1; Monday = 2; Tuesday = 3; Wednesday = 4; etc..

# This depends on how many selections are available for that day.
# Ex: if the first available hour is 12-2pm, then to select the noon slot you set HOUR_OF_DAY = 1
# On Tuesday for 5:45 pm, likely it will be HOUR_OF_DAY = 3
HOUR_OF_DAY = 1

FIRST_NAME = "Tara"
MIDDLE_NAME = "Christina"
LAST_NAME = "Virginillo"

# --------------------------------- FIRST WIDGET SCREEN ----------------------------------------------------------------

# tr[1] = first week of month; tr[2]  = second week of month
# td[3] = 3rd day of week (tuesday)
day_xpath = '//*[@id="start_date_calendar"]/div/table/tbody/tr['+str(WEEK_OF_MONTH)+']/td['+str(DAY_OF_WEEK)+']/a'
date = driver.find_element_by_xpath(day_xpath)
date.click()

# Set participant value to PARTICIPANT_NUM
participant_num = driver.find_element_by_id('pcount-pid-1-1109')
participant_num.send_keys(str(PARTICIPANT_NUM))

# THIS WILL ONLY WORK WHEN SELECT BUTTON IS AVAILABLE
xpath_select = '//*[@id="offering-page-select-events-table"]/tbody/tr['+str(HOUR_OF_DAY)+']/td[4]/a'
        
print("Done first sreen")

# --------------------------------- SECOND WIDGET SCREEN ----------------------------------------------------------------
first_name = driver.find_element_by_id("pfirstname-pindex-1-1")
first_name.send_keys(str(FIRST_NAME))

middle_name = driver.find_element_by_id("pmiddle-pindex-1-1")
middle_name.send_keys(str(MIDDLE_NAME))

last_name = driver.find_element_by_id("plastname-pindex-1-1")
last_name.send_keys(str(LAST_NAME))

