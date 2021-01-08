from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome=webdriver.Chrome()
chrome.get("C:\\Users\\mphpamatrasu2000\\Desktop\\uchihaBot\\test.html")

rowc=len(chrome.find_elements(By.XPATH,"/html/body/table/tbody/tr"))
print(rowc)

colc=len(chrome.find_elements(By.XPATH,"/html/body/table/tbody/tr[1]/td"))
print(colc)

print(chrome.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]").text)
