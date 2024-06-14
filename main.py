# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# import time

# URL = str(input('Enter the Video URL >> '))
# DRIVERS = int(input('Number of Drivers(Windows) >> '))
# driver = []
# BreakRate = 10 #sec
# PATH = "C:\Program Files (x86)\chromedriver-win64\chromedriver-win64\chromedriver.exe" #path of chromedriver

# for i in range(DRIVERS):
#     driver.append(webdriver.Chrome(PATH))
#     driver[i].get(URL)
#     action = ActionChains(driver[i])
#     action.send_keys(Keys.SPACE)
#     action.perform()
        
# while True:
#     time.sleep(BreakRate)
#     for j in range(DRIVERS):
#         driver[j].refresh()
#         action = ActionChains(driver[j])
#         action.send_keys(Keys.SPACE)
#         action.perform()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

# Use a raw string or double backslashes for the path
PATH = r'C:\Program Files (x86)\chromedriver-win64\chromedriver-win64\chromedriver.exe'  # Path of chromedriver

# Create a service object with the path to the chromedriver executabl
# e
service = Service(PATH)

URL = str(input('Enter the Video URL >> '))
DRIVERS = int(input('Number of Drivers(Windows) >> '))
driver = []
BreakRate = 10 #sec

for i in range(DRIVERS):
    # Initialize the Chrome webdriver with the service object
    driver_instance = webdriver.Chrome(service=service)
    driver.append(driver_instance)
    driver[i].get(URL)
    action = ActionChains(driver[i])
    action.send_keys(Keys.SPACE)
    action.perform()
        
while True:
    time.sleep(BreakRate)
    for j in range(DRIVERS):
        driver[j].refresh()
        action = ActionChains(driver[j])
        action.send_keys(Keys.SPACE)
        action.perform()

