#! /usr/bin/env python3.6
'''
for this script, you should run it using python3 with bs4 installed.
python 2 is not supported, because the urllib has been changed between 2 and 3.

you can use pip to install bs4

$ pip3 install beautifulsoup4

'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys

## generate page url

def generatePageUrl(totalNum, name):
    pageUrlList = []
    for i in range(totalNum):
        pageUrlList.append('http://images.qsfuli.com/category/tumblr/'+name+'/page/'+ str(i))
    return pageUrlList

def findTargetUrl(url):
    '''
    find all target urls from the given url,
    return a url list.
    '''
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'html.parser')
    aList = []
    aList = bsObj.findAll('a')
    
    styleList =[]
    for a in aList:
        if 'style' in a.attrs:
            styleList.append(a.attrs['style'])
    
    urlList = []
    for style in styleList:
        urlList.append(style[22:-2])
    
    return urlList

if __name__ == '__main__':
    '''
    run this script use formate bellow:

    $ python3 getImageUrl.py NAME TOTAL_NUM
    
    NAME is the subtitle of https://images.qsfuli.com.
    Now, there are 'qbyhx' 'wanimal' 'azhua' 'huafox' which you can choose
    TOTAL_NUM is the number of pages you want to scrap.

    For example:
    $ python getImageUrl.py qbyhx 100

    will scrap https://images.qsfuli.com/qbyhx/ for 0 - 100 pages.
    
    '''
    totalNum = int(sys.argv[2])
    # print (totalNum)
    
    name = sys.argv[1]
    
    pageUrlList = generatePageUrl(totalNum, name)
    urlList =[]
    
    for pageUrl in pageUrlList:
        urlList+=findTargetUrl(pageUrl)
    
    for url in urlList:
        print (url)
