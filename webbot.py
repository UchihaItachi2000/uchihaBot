# وارد کردن کتابخانه های سلنیوم
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# وارد کردن ماژول تایم
import time

# ایجاد یک درایور مجازی از مرورگر کروم
myChrome=webdriver.Chrome()
# باز کردن صفحه وب به مدت 3 ثانیه
myChrome.get("file:///C:/Users/mphpamatrasu2000/Desktop/uchihaBot/test.html")
#myChrome.find_element_by_css_selector("input[value=blue]").click()
#input_var=myChrome.find_element_by_css_selector("input[value=blue]")
#print(input_var.is_selected())
time.sleep(3)
