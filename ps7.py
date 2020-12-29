from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time

mychrome=webdriver.Chrome()
mychrome.get("C:\\Users\\mphpamatrasu2000\Desktop\\uchihaBot\\test.html")
time.sleep(3)
choices=mychrome.find_element(By.ID,"cars")
selectchoices=Select(choices)

#selectchoices.select_by_visible_text("Saab")
#selectchoices.select_by_index(3)
#selectchoices.select_by_value("car3")

#print(len(selectchoices.options))

all_sco=selectchoices.options

for op in all_sco:
    print(op.text)
