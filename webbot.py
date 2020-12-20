from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

mydriver=webdriver.Chrome()
mydriver.get("https://www.cnet.com/")
print(mydriver.title)
print(mydriver.current_url)
mydriver.find_element_by_xpath("/html/body/div[2]/span[1]/a").click()
#time.sleep(10)
#mydriver.close()
#mydriver.quit()
