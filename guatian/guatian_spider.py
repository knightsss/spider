# coding=utf-8
__author__ = 'shifeixiang'
import sys
import re
import urllib2
import requests
import json
from bs4 import BeautifulSoup
import bs4
import HTMLParser
import time

def get_base_url():
    url = "http://www.douban.com"
    # request1 = urllib2.Request("http://www.baidu.com")  # 已知，根据用户输入的公众号去搜索
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)
    # #写入文件
    # f_base_comment = open('wx_base_php.txt', 'w')
    # f_base_comment.write(base_html)
    # f_base_comment.close()
    # soup = BeautifulSoup(base_html)
    # try:
    #     mid_url = soup.find(href=re.compile("http://mp.weixin.qq.com/profile")).get('href')
    # except:
    #     # print "公众号不存在！"
    #     return None
    print html
    # print type(str(soup.body))
    # print str(soup.body)
    # return soup

if __name__ == '__main__':
    get_base_url()
