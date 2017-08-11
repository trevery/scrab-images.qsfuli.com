#! /usr/bin/env python3.6

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
    
    totalNum = int(sys.argv[2])
    print (totalNum)
    
    name = sys.argv[1]
    
    pageUrlList = generatePageUrl(totalNum, name)
    urlList =[]
    
    for pageUrl in pageUrlList:
        urlList+=findTargetUrl(pageUrl)
    
    for url in urlList:
        print (url)
