from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
# Python time sleep function is used to add delay in the execution of a program.

path = "C:/Users/sutha/Documents/selenium/chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service = s)
driver.get("https://www.google.com/")

time.sleep(2)

# XPath is a Selenium technique to navigate through a page's HTML structure.

box = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
box.send_keys("House Of Dragon")
box.send_keys(Keys.ENTER) # Keys.ENTER will automatically press the enter key
time.sleep(3)
driver.find_element_by_xpath("""//*[@id="kp-wp-tab-overview"]/div[3]/div/div/div/div/div/div[1]/div/a""").click()
time.sleep(2)
driver.save_screenshot("C:/Users/sutha/Documents/Python Scripts/House of Dragon/dragon.png")
#It will take the screenshot of the web page