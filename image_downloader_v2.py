#! python3
# image_downloader.py - downloads images from a photo-sharing site like
# Flickr or Imgur for a given category and their results
#
# Usage: python.exe image_downloader.py <photo-sharing site> "<category/search term>"
#        both <keywords> are necessary
#        <category/search term> should be in "" for multiple words
#        supported sites are: Imgur
# 06-01-2019 elective skill
#

import sys
import os
import requests
import bs4


def downloadPage(url):  # function for downloading the pages HTML
    res = requests.get(url)
    res.raise_for_status

    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    return soup


# save arguments from cmd line to variables
site = sys.argv[1]
term = sys.argv[2].strip('""')
os.makedirs('results', exist_ok=True)

# check which site is asked for and execute specific code
if site == 'Flickr':
    # implementation of Flickr failed first time, the new version focuses on imgur
    # Flickr follows later
    print("Flickr is currently not supported.")
elif site == 'Imgur':
    # change term to needed layout
    term.replace(" ", "+")
    url = 'https://imgur.com/search?q=' + term
    print('URL:', url)
    # get the soup for the specific url
    soup = downloadPage(url)

    # Find urls of image detail
    imagesElem = soup.select('a.image-list-link img')
    if imagesElem == []:
        # if there are no results
        print('There are no images for this term.')
    else:
        # save every found image
        for image in imagesElem:
            # get the specific urls for the images
            imageUrl = image.get('src')
            imageUrl = 'http:' + imageUrl
            # just some information for user
            print('Downloading image %s...' % (imageUrl))

            resImage = requests.get(imageUrl)
            resImage.raise_for_status()
            # actually saving the image to hard drive
            imageFile = open(os.path.join('results', os.path.basename(imageUrl)), 'wb')
            for chunk in resImage.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
    print("Done.")
else:
    print("This site is not supported.")
