#! python3
# strong_password_detection.py - This program is for detecting
# a strong password
# 14-10-2019 elective skill

import re

digitCheck = re.compile(r'\d')
lowercaseCheck = re.compile('[a-z]')
uppercaseCheck = re.compile('[A-Z]')

password = input("Enter password to check: ")

while True:
    if len(password) >= 8:
        if len(digitCheck.findall(password)) > 0:
            if len(lowercaseCheck.findall(password)) > 0:
                if len(uppercaseCheck.findall(password)) > 0:
                    print('Your password is strong!')
                    exit()

    print('''Your password is not strong enough!
    A strong password contains:
    - at least 8 characters
    - both uppercase and lowercase
    - at least one digit
    ''')

    password = input("Try again: ")
