# How to use it

## Install bs4

For this script, you should use python3 with bs4 model installed.

To install bs4, use command bellow.
```
$ pip3 install beautifulsoup4
```
## Clone 

In your command line. Clone this repo by using:

```
$ git clone "https://github.com/trevery/scrab-images.qsfuli.com/"
```


## Run this script

First, change directory to this folder

```
$ cd scrab-images.qsfuli.com
```

To run this script, please use formate bellow:

$ python3 getImageUrl.py NAME TOTAL_NUM

NAME is the subtitle of https://images.qsfuli.com.
Now, there are 'qbyhx' 'wanimal' 'azhua' 'huafox' which you can choose
TOTAL_NUM is the number of pages you want to scrap.

For example:
```
$ python getImageUrl.py qbyhx 2
```
will scrap http://images.qsfuli.com/category/tumblr/qbyhx/ for 0 - 100 pages.
