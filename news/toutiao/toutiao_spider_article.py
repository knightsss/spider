##coding=utf-8
__author__ = 'shifeixiang'

import sys
import requests
from bs4 import BeautifulSoup
sys.path.append('E:\\Python\\spider\\news\\toutiao')
from toutiao_phantomjs_spider import redis_connect,pop_redis_list

def get_toutiao_article(article_url_list):

    for sub_url in article_url_list:
        # time.sleep(2)
        print 'sub_url',sub_url
        url = 'http://www.toutiao.com' + str(sub_url)
        print url
        response = requests.get(url)
        soup  = BeautifulSoup(response.text)
        # print soup
        #标题
        try:
            try:
                title = soup.find(class_='article-title')
            except:
                title = soup.find(class_='conText')
            title = unicode(title.string).encode('utf-8')
        except:
            title = ""
        print "title: ",title

        #内容
        try:
            content_all = ""
            try:
                contents = soup.find(class_='article-content')
            except:
                contents = soup.find(id='text')

            for content in contents.stripped_strings:
                content_all = content_all + content + "\n"
        except:
            content = ""
        print "content:  ",content_all

        #来源
        try:
            try:
                src = soup.find(class_='src')
            except:
                src = soup.find(id='source_baidu')
            src = unicode(src.string).encode('utf-8').replace('\n','')
        except:
            src = ""
        print "src: ",src

        #时间
        try:
            try:
                time = soup.find(class_='time')
            except:
                time = soup.find(id='pubtime_baidu')
            time = unicode(time.string).encode('utf-8')
        except:
            time = ""
        print "time: ",time

        #关键词
        try:
            keyword_all = ""
            keywords = soup.find(class_='label-list')
            for keyword in keywords.stripped_strings:
                keyword_all = keyword_all + keyword + ','
        except:
            keyword = ""
        print "keyword: ",keyword_all

        #正文dom
        try:
            content_dom = soup.find(class_='article-content')
        except:
            content_dom = ""
        print content_dom


if __name__ == '__main__':

    #取一条新闻URL
    #获取新闻内容
    #调用接口
    #获取关键字
    #爬虫维基百科
    #获取内容
    #存入数据库
    redis_conn = redis_connect()
    redis_list_name = 'n_t_test_tmp'
    article_url_list = []
    for i in range(3):
        url_args = pop_redis_list(redis_conn,redis_list_name)
        article_url_list.append(url_args)
        print url_args
    get_toutiao_article(article_url_list)