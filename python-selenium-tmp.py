#!/usr/bin/python

import codecs
import sys
import types
import time

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://ADDRESS')
elem = driver.find_element_by_name('login_tuid')
elem.send_keys('USER')
elem = driver.find_element_by_name('login_pwd')
elem.send_keys('PASSWORD')
driver.find_element_by_name('login').click()
#print driver.page_source

time.sleep(3)

driver.switch_to_default_content()
driver.switch_to_frame("FRAME NAME")
#print driver.page_source

checkboxes = driver.find_element_by_name('chkInput')
checkboxes = driver.find_elements_by_xpath("//input[@name='chkInput']")
for checkbox in checkboxes:
    if not checkbox.is_selected():
       checkbox.click()
       break

parent_h = driver.current_window_handle

time.sleep(1)
buttons = driver.find_elements_by_css_selector("button")
for button in buttons:
    onclick_text = button.get_attribute('onClick')
    #print onclick_text
    if 'FUNCTION-NAME' in onclick_text:
        button.click()
        break

handles = driver.window_handles
handles.remove(parent_h)
driver.switch_to_window(handles.pop())
print driver.page_source

#time.sleep(4)

#driver.switch_to_alert()
#print driver.page_source
