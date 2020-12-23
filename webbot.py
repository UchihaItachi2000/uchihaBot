# Selenium Library
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

mydriver=webdriver.Chrome()

mydriver.get("https://www.selenium.dev/documentation/en/")
print(mydriver.current_url)
time.sleep(3)
mydriver.find_element_by_xpath("//*[@id='sidebar']/div[2]/ul/li[1]/a").click()
print(mydriver.current_url)
time.sleep(3)
mydriver.back()
print(mydriver.current_url)
time.sleep(3)
mydriver.forward()
#print(mydriver.title)
#print(mydriver.current_url)

#time.sleep(10)
#mydriver.close()
#mydriver.quit()
