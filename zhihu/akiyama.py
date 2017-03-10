# -*- coding: utf-8 -*-
__author__ = 'akiyama'
import urllib
import urllib2
import re
import json
from com.learn.zhihuSearch.topic import *
from com.learn.zhihuSearch.content import *
import cookielib

def getTopics():
    zhihuTopics = []
    url = 'https://www.zhihu.com/topics'
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    request = urllib2.Request(url)
    response = opener.open(request)
    pattern = re.compile('<li.*?data-id="(.*?)"><a.*?>(.*?)</a></li>',re.S)
    results = re.findall(pattern,response.read().decode('utf-8'))
    for n1 in results:
        print n1[0],n1[1]
        topic = Topic(n1[0],n1[1])
        zhihuTopics.append(topic)
    return zhihuTopics

def getSubTopic(topic):
    url = 'https://www.zhihu.com/node/TopicsPlazzaListV2'
    isGet = True;
    offset = -20;
    contents = []
    while isGet:
        offset = offset + 20
        values = {'method': 'next', 'params': '{"topic_id":'+topic.id+',"offset":'+str(offset)+',"hash_id":""}'}
        try:
            data = urllib.urlencode(values)
            request = urllib2.Request(url,data,headers)
            response = urllib2.urlopen(request)
            json_str = json.loads(response.read().decode('utf-8'))
            # 将获取到的数组转换成字符串
            topicMsg = '.'.join(json_str['msg'])
            pattern = re.compile('<strong>(.*?)</strong>.*?<p>(.*?)</p>',re.S)
            results = re.findall(pattern,topicMsg)
            if len(results) ==0:
                isGet =False
            for n in results:
                content = Content(n[0],n[1])
                contents.append(content)
                print n[0],'->'+n[1]
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"错误原因",e
    file = open(topic.name+'.txt','w')
    wiriteLog(contents,file)
    return contents

def wiriteLog(contentes,file):
    for content in contentes:
        file.writelines(('\n'+content.name+'->'+content.content).encode("UTF-8"))

print '开始拉取数据...\n'
headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0',
           'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
           'X-Requested-With':'XMLHttpRequest',
           'Referer':'https://www.zhihu.com/topics',
           'Cookie':'__utma=51854390.517069884.1416212035.1416212035.1416212035.1; q_c1=c02bf44d00d240798bfabcfc95baeb56|1455778173000|1416205243000; _za=b1c8ae35-f986-46a2-b24a-cb9359dc6b2a; aliyungf_tc=AQAAAJ1m71jL1woArKqF22VFnL/wRy6C; _xsrf=9d494558f9271340ab24598d85b2a3c8; cap_id="MDNiMjcwM2U0MTRhNDVmYjgxZWVhOWI0NTA2OGU5OTg=|1455864276|2a4ce8247ebd3c0df5393bb5661713ad9eec01dd"; n_c=1; _alicdn_sec=56c6ba4d556557d27a0f8c876f563d12a285f33a'
           }
i = 0
topics = getTopics()
for topic in topics:
    content = getSubTopic(topic)
    i +=len(content)
print '知乎总话题数为：'+str(i)
print '拉取数据结束'
