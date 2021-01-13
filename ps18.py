from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

opt=Options()
myprefs = {'safebrowsing.enabled': 'False'}
opt.add_experimental_option("prefs",myprefs)

chrome=webdriver.Chrome(options=opt)
chrome.get("https://www.videolan.org/vlc/download-windows.html")

chrome.find_element(By.ID,"downloadButton2").click()
