# وارد کردن کتابخانه های سلنیوم
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# وارد کردن ماژول تایم
import time

# عدم قرار گرفتن درایور در مسیر اصلی
#myChrome=webdriver.Chrome(executable_path="C:\\Users\\mphpamatrasu2000\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver.exe")

# ایجاد یک درایور مجازی از مرورگر کروم
myChrome=webdriver.Chrome()
# باز کردن صفحه وب به مدت 3 ثانیه
myChrome.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
#myChrome.maximize_window()
#myChrome.find_element_by_xpath("//*[@id='continue']")
emailEle=myChrome.find_element_by_id("ap_email")
if emailEle.is_displayed()==True and emailEle.is_enabled()==True :
    emailEle.send_keys("my name")
if myChrome.find_element_by_xpath("//*[@id='continue']").click()==None:
    myChrome.find_element_by_xpath("//*[@id='createAccountSubmit']").click()
time.sleep(3)
