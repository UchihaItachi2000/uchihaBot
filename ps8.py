# وارد کردن کتابخانه های سلنیوم
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome=webdriver.Chrome()
chrome.get("C:\\Users\\mphpamatrasu2000\\Desktop\\uchihaBot\\test.html")

links=chrome.find_elements(By.TAG_NAME,"a")

#print("\n\n",len(links))

#for items in links:
#    print(items.text)


#chrome.find_element(By.LINK_TEXT,'my result page').click()
chrome.find_element(By.PARTIAL_LINK_TEXT,'Mi').click()
