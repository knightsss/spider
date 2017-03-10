#coding=utf-8
__author__ = 'shifeixiang'

import urllib2
import requests

url = 'http://map.baidu.com/'

# request = urllib2.Request(url)
# html = urllib2.urlopen(request).read()
# print html

response = requests.get(url)
print response.content