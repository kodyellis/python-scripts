#!/usr/bin/python
from selenium import webdriver
import time
driver = webdriver.Firefox()
website ="http://www.msn.com/"
driver.get(website)
varf = driver.find_elements_by_css_selector('body')
time.sleep(5)
varf.send_keys('\uE035')
#driver.refresh()
