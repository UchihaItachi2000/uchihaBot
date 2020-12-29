# وارد کردن کتابخانه های سلنیوم
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# وارد کردن ماژول تایم
import time

# ایجاد درایو مجازی مرورگر
mychrome=webdriver.Chrome()
mychrome.get("C:\\Users\\mphpamatrasu2000\\Desktop\\uchihaBot\\test.html")

#بررسی تعداد
texts=mychrome.find_elements(By.CLASS_NAME,'mytext')
print(len(texts))

#ارسال اطلاعات
time.sleep(5)
mychrome.find_element(By.ID,"txtname").send_keys("testname")
time.sleep(5)
mychrome.find_element(By.ID,"txtfamily").send_keys("testfamily")
time.sleep(5)
mychrome.find_element(By.ID,"txtemail").send_keys("name@company.com")
time.sleep(5)
mychrome.find_element(By.ID,"txtpassword").send_keys("123456")
time.sleep(5)
mychrome.find_element(By.NAME,"login").click()
