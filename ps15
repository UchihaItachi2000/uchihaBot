from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

def defweb():
    op = webdriver.ChromeOptions()
    op.add_argument("--disable-notifications")
    prefs = {"profile.default_content_setting_values.geolocation" :2}
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    op.add_experimental_option("prefs",prefs)
    op.add_argument("disable-infobars")
    op.add_argument("--disable-extensions")
    return op


chrome=webdriver.Chrome(options=defweb())
chrome.get("https://www.tgju.org/")
chrome.maximize_window()


chrome.find_element(By.XPATH,"//*[@id='popup-layer-container']/div[2]/a").click()

title=chrome.find_element(By.XPATH,"//*[@id='main-header']/div[3]/div[1]/div[2]/ul/li[1]/a")
subtitle=chrome.find_element(By.XPATH,"//*[@id='main-header']/div[3]/div[1]/div[2]/ul/li[1]/div/div/ul/li[2]/ul[1]/li[3]/a")

act=ActionChains(chrome)
act.move_to_element(title).move_to_element(subtitle).click().perform()
