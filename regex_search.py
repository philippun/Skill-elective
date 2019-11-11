#! python3
# regex_search.py - opens all .txt files in a folder and finds all user-supplied
# regular expressions
# Usage: python.exe regex_search.py <directory> <regex expression>
#        this applies program to folder with specified expression
# 11-11-2019 elective skill

import sys
import re
import glob
import os

path = sys.argv[1].strip('"')
expression = sys.argv[2]
search = re.compile(expression)

# loop over all text files
for filename in glob.glob(os.path.join(path, '*.txt')):
    file = open(filename)
    content = file.read()
    file.close()
    # loop over all lines of text files
    for line in content.splitlines():
        # check line for search expression
        result = search.findall(line)
        if len(result) > 0:
            print('"', line, '"', filename)
