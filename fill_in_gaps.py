#! python3
# fill_in_gaps.py - finds files with a given prefix in a directory and recognizes
# gaps in the numbering (e. g. spam001.txt, spam002.txt, spam003.txt)
# additionally the program can rename the files to close the gap
# Usage: python.exe fill_in_gaps.py <directory> <prefix>
#        both <keywords> are necessary
# 02-12-2019 elective skill

import sys
import re
import os

dir = sys.argv[1].strip('"')
prefix = sys.argv[2].strip('""')
search = re.compile(prefix)
# change working directory
os.chdir(dir)

# define some variables
count = 0
toggle = False
answer = ''
filenameArray = []

print('filename, count, fitting?')
# loop through specified directory
for foldername, subfolders, filenames in os.walk(dir):
    for filename in filenames:
        # if filename contains prefix
        if len(search.findall(filename)) > 0:
            # append array with found filename
            filenameArray.append(filename)
            # increase count
            count += 1
            # extract extension and filename without it
            cleanFilename, file_extension = os.path.splitext(filename)
            # get the count of the filename and convert to integer, then compare
            if int(cleanFilename.strip(prefix)) == count:
                fittingFilename = 'Fitting'
            # if the first statement did not work, filename is unfitting
            else:
                fittingFilename = 'Unfitting'
                toggle = True
            # print out list with filenames and if their name is fitting
            print(filename, ',', cleanFilename.strip(prefix), ',', fittingFilename)

# check if there are unfitting filenames
if toggle:
    # ask user if he wants them to be corrected
    print('Do you want to rename the files correctly? (Y/N): ')
    answer = input()

# correct them if user wants to
if answer == 'Y':
    # correct count
    count = 1
    for item in filenameArray:
        # rename files
        os.rename(item, prefix + str(count) + file_extension)
        # increase count
        count += 1
    print('Done')
