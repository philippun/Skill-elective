#! python3
# command_line_emailer.py - takes an email address and string of text on the
# command line and sends an email to the given address containing the given string
#
# Usage: python.exe command_line_emailer.py <email> "<content>"
#        both <keywords> are necessary
#        <content> should be in ""
# 16-12-2019 elective skill
# ChromeDriverManager().install()
# email: testingautomation@mail.de password: ######

import sys
import time
# import selenium module which controls the browser
from selenium import webdriver

# read command arguments
mail = sys.argv[1]
content = sys.argv[2].strip('""')

# start an instance of the browser
browser = webdriver.Chrome()
browser.get('http://www.mail.de')

# wait 3 seconds
time.sleep(3)

# find login name field and fill in
emailElement = browser.find_element_by_name('loginName')
emailElement.send_keys('testingautomation@mail.de')

# find login password field and fill in, then submit
passwordElement = browser.find_element_by_name('loginPassword')
passwordElement.send_keys('######')
passwordElement.submit()

time.sleep(2)

# start new email
emailElement = browser.find_element_by_name('email')
emailElement.click()

time.sleep(3)

# fill in given mail to send to
toElement = browser.find_element_by_name('to')
toElement.send_keys(mail)

time.sleep(1)

# fill in subject line with given content
subjectElement = browser.find_element_by_name('subject')
subjectElement.send_keys(content)

time.sleep(1)

# contentElement = browser.find_element_by_id('tinymce')
# contentElement.send_keys('dummy')
#
# time.sleep(1)

# send mail
sendElement = browser.find_element_by_name('sendMessage')
sendElement.click()

# close browser
browser.quit()
