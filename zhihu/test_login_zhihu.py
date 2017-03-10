#coding=utf-8
__author__ = 'shifeixiang'

import requests
import urllib2

url = "http://www.zhihu.com"
url2 = "http://www.baidu.com"

headers = {
    'Request URL':'https://www.zhihu.com/',
    'Request Method':'GET',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',

    'Connection':'keep-alive',
    # 'Content-Length':'15',
    'Content-Type':'text/html; charset=UTF-8',
    # 'Cookie':'LOVEAPP_SESSID=9ba3ea1f19854f7688b6a5581fc99953a66b1f3e; _gat=1; _ga=GA1.2.1450567678.1478597084; lang=CN',
    'Host':'www.zhihu.com',
    # 'Origin':'https://www.ipip.net',
    'Referer':'https://www.zhihu.com/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'
}

# response = requests.get(url)
# requests.get(url=url,headers = headers)


# response = urllib2.urlopen(url)
# html = response.read()
# # print response.content
# print html

from bs4 import BeautifulSoup

url = "https://www.zhihu.com/explore/recommendations"
response = urllib2.urlopen(url)
html = response.read()

soup = BeautifulSoup(html)
links = soup.find_all(class_='post-link')
for link in links:
    print link
# print html