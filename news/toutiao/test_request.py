#coding=utf-8
__author__ = 'shifeixiang'

import requests
import urllib2

headers = {
    # 'Request URL':'https://www.toutiao.com/',
    'Request Method':'GET',
    'Accept':'text/javascript, text/html, application/xml, text/xml, */*',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    # 'Content-Length':'15',
    'Content-Type':'application/x-www-form-urlencoded',
    # 'Cookie':'LOVEAPP_SESSID=9ba3ea1f19854f7688b6a5581fc99953a66b1f3e; _gat=1; _ga=GA1.2.1450567678.1478597084; lang=CN',
    'Host':'www.toutiao.com',
    # 'Origin':'https://www.ipip.net',
    'Referer':'https://www.toutiao.com/news_military/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
}

url = 'https://www.toutiao.com/api/pc/feed/?category=news_military&utm_source=toutiao&widen=1&max_behot_time=1488943512&max_behot_time_tmp=1488943512&tadrequire=true&as=A175E84B0F47FD9&cp=58BF47AF5D996E1'

body = {
        'category':'news_military',
        'utm_source':'toutiao',
        'widen':'1',
        'max_behot_time':'1488943512',
        'max_behot_time_tmp':'1488943512',
        'tadrequire':'true',
        'as':'A175E84B0F47FD9',
        'cp':'58BF47AF5D996E1',
}

headers['Request URL'] = url
headers['Remote Address'] = '121.14.13.44:443'
print headers
print body

import urllib

def test():
    global body
    body = urllib.urlencode(body)
    request = urllib2.Request(url, data=body)
    response = urllib2.urlopen(request)
    html = response.read()
    print type(html)
    with open('json7.txt','w') as f:
        f.write(html)
    print html


# response = requests.get(url=url, headers=headers, data=body)
# response_dict = response.text
# print response_dict


if __name__ == '__main__':
    url = 'http://www.toutiao.com/a6395377898034905345/'
    response = requests.get(url)
    print response.text