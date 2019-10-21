#! python3
# regex_version_of_strip_function.py - This program is supposed to
# have the same function as strip()
# 21-10-2019 elective skill

import re


# function for stripping the phrase of the given characters
def stripCopy(phrase, charsToBeRemoved):
    if charsToBeRemoved == '':
        strippedPhrase = re.sub(r"^\s+|\s+$", '', phrase)  # | for OR condition
    else:
        strippedPhrase1 = re.sub(r'^[%s]+' % charsToBeRemoved, '', phrase)
        strippedPhrase = re.sub(r'[%s]+$' % charsToBeRemoved, '', strippedPhrase1)
    return strippedPhrase


word = input("Enter phrase you wanna strip: ")
removeWhat = input("What do you wanna remove: ")
print('Stripped word: ', stripCopy(word, removeWhat), sep='')
