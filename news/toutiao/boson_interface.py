##coding=utf-8
__author__ = 'shifeixiang'

import json
import requests
from bs4 import BeautifulSoup


def test_emotion():
    SENTIMENT_URL = 'http://api.bosonnlp.com/sentiment/analysis'
    # 注意：在测试时请更换为您的API Token
    headers = {'X-Token': 'B10dxhtR.13489.BjImZQNV6D6K'}

    s = ['他是个英雄', '美好的世界']
    data = json.dumps(s)
    resp = requests.post(SENTIMENT_URL, headers=headers, data=data.encode('utf-8'))

    print(resp.text)
if __name__ == '__main__':
    word = '和平'
    url = 'https://zh.wikipedia.org/wiki/' + str(word)
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html)
    contents = soup.find(id='bodyContent').stripped_strings
    tmp_list = ""
    for content in contents:
        tmp_list  = tmp_list + content

    print tmp_list