#! python3
# find_large_files.py - finds large files in a given directory and prints
# their absolute path to the screen
# Usage: python.exe find_large_files.py <directory> <size>
#        only first <keywords> is necessary
#        size in MegaByte
# 25-11-2019 elective skill

import sys
import os

# check if user wants to use own size
dir = sys.argv[1].strip('"')
if len(sys.argv) > 2:
    size = float(sys.argv[2]) * (1024 ** 2)
else:
    size = 100 * (1024 ** 2)

print('\n')

# walk through directory
for foldername, subfolders, filenames in os.walk(dir):
    for filename in filenames:
        path = foldername + "\\" + filename
        # if condition fulfilled print out path
        if os.path.getsize(path) >= size:
            print(path)
            print('Size: ', os.path.getsize(path) / (1024 ** 2), 'MB')

print('\nDone')
