 # GroundUp Automated Booking Script
 # Owner : Anonymous
 # Last Update : February 6th, 2021
 #
 # Requirements: Selenium, Chromedriver
 # 
 # Selenium docs for reference : https://selenium-python.readthedocs.io/
 
from selenium import webdriver
import time

# Select proper URL depending on your choice of reservation
MEMBER_URL = "https://app.rockgympro.com/b/widget/?a=offering&offering_guid=a2015138518d4e389995ee21526c682d&widget_guid=e8cacb9641fa4f6ea12a176adc3a3570&random=601c44ac5b25d&iframeid=rgpiframe601c43cdd5d13&mode=e&course_guid=ca4ec882af24e499d7691d2bf537861b6e519e60"
NON_MEMBER_URL = "https://app.rockgympro.com/b/widget/?a=offering&offering_guid=fd63ba3934f44647a1151b4ef6507d77&widget_guid=e8cacb9641fa4f6ea12a176adc3a3570&random=601c56694c33c&iframeid=rgpiframe601c43cdd5d13&mode=e&course_guid=ca4ec882966b50e97b44e1832333108e6169537b"

# Connect to chromedriver & load website
CHROMEDRIVER_PATH = r'C:/Program Files/Chromedriver/chromedriver.exe'

#options = webdriver.ChromeOptions() 
#options.add_argument("start-maximized")
#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
driver.get(NON_MEMBER_URL)

# ----------------------------------Global Variables --------------------------------------------------------------------
# Script not set to accept 2 participants (yet)
PARTICIPANT_NUM = 1
WEEK_OF_MONTH = 2
DAY_OF_WEEK = 3 # Sunday = 1; Monday = 2; Tuesday = 3; Wednesday = 4; etc..

# This depends on how many selections are available for that day.
# Ex: if the first available hour is 12-2pm, then to select the noon slot you set HOUR_OF_DAY = 1
# On Tuesday for 5:45 pm, it will likely be HOUR_OF_DAY = 3
HOUR_OF_DAY = 3

FIRST_NAME = "Tara"
MIDDLE_NAME = "Christina"
LAST_NAME = "Virginillo"
BIRTH_MONTH = "Apr"
BIRTH_DAY = 26
BIRTH_YEAR = 1997

EMAIL = "taravirginillo@gmail.com"
PHONE = "6692684951"

# --------------------------------- FIRST WIDGET SCREEN ----------------------------------------------------------------

# tr[1] = first week of month; tr[2]  = second week of month
# td[3] = 3rd day of week (tuesday)
day_xpath = '//*[@id="start_date_calendar"]/div/table/tbody/tr['+str(WEEK_OF_MONTH)+']/td['+str(DAY_OF_WEEK)+']/a'
date = driver.find_element_by_xpath(day_xpath)
date.click()

# Set participant value to PARTICIPANT_NUM
participant_num = driver.find_element_by_id('pcount-pid-1-1109')
participant_num.send_keys(str(PARTICIPANT_NUM))

# THIS WILL ONLY WORK WHEN SELECT BUTTON IS AVAILABLE.
xpath_to_second_screen = '//*[@id="offering-page-select-events-table"]/tbody/tr['+str(HOUR_OF_DAY)+']/td[4]/a'
first_screen_select = driver.find_element_by_xpath(xpath_to_second_screen)
first_screen_select.click()

print("Done first sreen")

# Wait for widget to load (my script is #toofast)
time.sleep(1)

# --------------------------------- SECOND WIDGET SCREEN ----------------------------------------------------------------
first_name = driver.find_element_by_id("pfirstname-pindex-1-1")
first_name.send_keys(str(FIRST_NAME))

middle_name = driver.find_element_by_id("pmiddle-pindex-1-1")
middle_name.send_keys(str(MIDDLE_NAME))

last_name = driver.find_element_by_id("plastname-pindex-1-1")
last_name.send_keys(str(LAST_NAME))

birth_month = driver.find_element_by_id("participant-birth-pindex-1month")
birth_month.send_keys(str(BIRTH_MONTH))

birth_day = driver.find_element_by_id("participant-birth-pindex-1day")
birth_day.send_keys(str(BIRTH_DAY))

birth_year = driver.find_element_by_id("participant-birth-pindex-1year")
birth_year.send_keys(str(BIRTH_YEAR))

# THIS WILL ONLY WORK WHEN SELECT BUTTON IS AVAILABLE.
xpath_to_third_screen = '//*[@id="theform"]/a[2]'
to_third_screen = driver.find_element_by_xpath(xpath_to_third_screen)
to_third_screen.click()

print("Done second screen")

# Wait for widget to load (my script is #toofast)
time.sleep(1)

# --------------------------------- THIRD WIDGET SCREEN ----------------------------------------------------------------

email = driver.find_element_by_id("customer-email")
email.send_keys(str(EMAIL))

phone = driver.find_element_by_id("customer-phone")
phone.send_keys(str(PHONE))

xpath_iagree_1 = '//*[@id="theform"]/fieldset[4]/div[2]/input'
xpath_iagree_2 = '//*[@id="theform"]/fieldset[4]/div[4]/input'

# Agree to all terms & conditions
iagree_1 = driver.find_element_by_xpath(xpath_iagree_1)
iagree_1.click()

iagree_2 = driver.find_element_by_xpath(xpath_iagree_2)
iagree_2.click()

print("Done third screen.")
# You are done the form. Click the "I'm not a bot" and you will be reserved!

# Next Steps : 
# https://stackoverflow.com/questions/58872451/how-can-i-bypass-the-google-captcha-with-selenium-and-python
# https://stackoverflow.com/questions/53917157/find-the-recaptcha-element-and-click-on-it-python-selenium/53917309#53917309
# https://sqa.stackexchange.com/questions/33219/how-to-avoid-triggering-google-captcha-while-browsing-in-a-selenium-driven-brows

# Notes : the code below produces fading images on recaptcha (highest level of recaptcha). 
#  Only 2 sets of images are produced when not attempting to click on recaptcha thru selenium (time to complete form = 1 minute)

#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC

#WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]'))).click()

#print("You are for sure not a robot!")

