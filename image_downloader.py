#! python3
# image_downloader.py - downloads images from a photo-sharing site like
# Flickr or Imgur for a given category and their results
#
# Usage: python.exe image_downloader.py <photo-sharing site> "<category/search term>"
#        both <keywords> are necessary
#        <category/search term> should be in "" for multiple words
#        supported sites are: Flickr
# 26-12-2019 elective skill

import sys
import os
import requests
import bs4


def downloadPage(url):  # function for downloading the pages HTML
    res = requests.get(url)
    res.raise_for_status

    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    return soup


site = sys.argv[1]
term = sys.argv[2].strip('""')
os.makedirs('results', exist_ok=True)

if site == 'Flickr':
    url = 'https://www.flickr.com/search/?text=' + term
    print('URL:', url)
    soup = downloadPage(url)

    # Find urls of image detail
    imagesElem = soup.select('div.photo-list-photo-interaction a')
    if imagesElem == []:
        print('There are no images for this term.')
    else:
        for element in imagesElem:
            imageDetailUrl = 'https://www.flickr.com' + imagesElem[element].get('href')
            res = requests.get(imageDetailUrl)
            res.raise_for_status

            soupImage = bs4.BeautifulSoup(res.text)
            imageElem = soup.select('.zoom-photo-container.zoom-level-1 img')
            if imageElem == []:
                print('Specific image not found.')
            else:
                imageUrl = imageElem[0].get('src')
                print('Downloading image %s...' % (imageUrl))
                resImage = requests.get(imageUrl)
                res.raise_for_status()

            imageFile = open(os.path.join('results', os.path.basename(imageUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
    print('Done.')
elif site == 'Imgur':
    print("Imgur is currently not supported.")
else:
    print("This site is not supported.")
