#! python3
# selective_copy.py - copies files with a specified extension from a folder tree
# to another folder
# Usage: python.exe selective_copy.py <source_folder> <extension> <destination_folder>
#        all <keywords> are necessary
# 18-11-2019 elective skill

import sys
import os
import shutil

# get keywords
source = sys.argv[1].strip('"')
extension = sys.argv[2]
destination = sys.argv[3].strip('"')

# get current working directory
cwd = os.getcwd()
# change directory to the source folder
os.chdir(source)

# loop through folder tree
for foldername, subfolders, filenames in os.walk(source):
    for filename in filenames:
        dummy, file_extension = os.path.splitext(filename)
        # every time there is a file with specific extension copy it
        if file_extension == extension:
            shutil.copy(foldername + "\\" + filename, destination)

# os.chdir(cwd)
print('Done')
