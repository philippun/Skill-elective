#! python3
# mad_libs.py - Reads a text file and lets the user add their own text anywhere
# the word ADJECTIVE, NOUN, ADVERB, or VERB appears in it.
# Usage: python.exe mad_libs.py <textfile> - applies program to specific text textfile
#        after that follow instructions in command prompt
# 04-11-2019 elective skill

import sys

# open, read and close a file after saving its content to a string variable
file = open(sys.argv[1])
content = file.read()
file.close()
# split the string into words
words = content.split()
newContent = []
count = 0

# check for the keywords and then prompt the user to give substitutes
for word in words:
    if word.rstrip('.,!?:;"') == 'ADJECTIVE' or word.rstrip('.,!?:;"') == 'NOUN' or word.rstrip('.,!?:;"') == 'ADVERB' or word.rstrip('.,!?:;"') == 'VERB':
        substitute = input('Enter an {}:\n'.format(word.lower().strip('.,')))
        substitute += word.lstrip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        count += 1
    else:
        substitute = word
    newContent.append(substitute)

# join the words again
separator = ' '
newContent = separator.join(newContent)

# write new content to file
file = open(sys.argv[1], 'w')
file.write(newContent)
file.close()

# print out the programs results
if count > 0:
    print('Words have been substituted!')
else:
    print('No keywords to subtitute!')
