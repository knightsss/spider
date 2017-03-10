#coding=utf-8
__author__ = 'shifeixiang'
import requests
import urllib2
import json
from pprint import pprint
from bs4 import BeautifulSoup
import time
import simplejson

#推荐的首页：
#https://www.toutiao.com/api/pc/feed/?category=__all__&utm_source=toutiao&widen=1&max_behot_time=1488873478&max_behot_time_tmp=1488873478&tadrequire=false&as=A17588BBBEF6FEB&cp=58BE063F3E2B8E1


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

def test_request():
    global headers


    url = 'http://www.toutiao.com/a6394633787259584770/'
    response = requests.get(url,headers=headers)
    soup  = BeautifulSoup(response.text)
    # print soup
    title = soup.find(class_='article-title')
    content = soup.find(class_='article-content')
    print "title: ",title.string
    print "content:  ",
    for i in content.stripped_strings:
        print i
    # print content

def test_url():
    global headers
    url = "http://www.toutiao.com/a6394633787259584770/"
    request = urllib2.Request(url=url,headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    print html

def test_pic():

    global headers
    url = "http://www.toutiao.com/search_content/?offset=20&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&_=1480675595492"
    request = urllib2.Request(url=url,headers=headers)
    with request.urlopen(url) as res:
        d = json.loads(res.read().decode())
        print(d)

from selenium import webdriver
import os
def test_ajax():

    import time
    driver = webdriver.PhantomJS('E:\\phantomjs\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs')
    # F:\auto_windows\atom-windows\Atom\chromedriver
    # chrome_driver = os.path.abspath(r"D:\云盘\360云\360云盘\我的自动双向同步文件夹\01-PersonalInfo\DataGuru\12-软件自动化测试Selenium2\1-课程\练习代码_Python版本\Selenium_python\Files\chromedriver.exe")
    # os.environ["webdriver.chrome.driver"] = chrome_driver
    # driver = webdriver.Chrome(chrome_driver)


    # chrome_driver = os.path.abspath(r"F:\auto_windows\atom-windows\Atom\new_chrome\chromedriver.exe")   #谷歌浏览器位置
    # os.environ["webdriver.chrome.driver"] = chrome_driver            #设置环境变量
    #
    # driver = webdriver.Chrome(chrome_driver)             #webdriver获取
    # driver=webdriver.Chrome(executable_path='F:\auto_windows\atom-windows\Atom\new_chrome\chromedriver.exe')

    # driver = webdriver.Firefox()
    #webdriver中的PhantomJS方法可以打开一个我们下载的静默浏览器。
    #输入executable_path为当前文件夹下的phantomjs.exe以启动浏览器
    # driver =webdriver.PhantomJS(executable_path="phantomjs.exe")

    #使用浏览器请求页面
    # driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
    driver.get("https://www.toutiao.com/news_military/")
    #加载3秒，等待所有数据加载完毕
    time.sleep(3)
    #通过id来定位元素，
    #.text获取元素的文本数据
    # print driver.find_element_by_id('content').text

    # for i in range(3):
    #     js1 = 'return document.body.scrollHeight'
    #     js2 = 'window.scrollTo(0, document.body.scrollHeight)'
    #     old_scroll_height = 0
    #     while(driver.execute_script(js1) > old_scroll_height):
    #         print "下拉"
    #         old_scroll_height = driver.execute_script(js1)
    #         driver.execute_script(js2)
    #         time.sleep(3)
    # js="var q=document.documentElement.scrollTop=10000"
    for i in range(5):
        print "pull ",str(i)
        js="var q=document.body.scrollTop=" + str((i+1)*1000)
        driver.execute_script(js)
        time.sleep(3)
    # print "pull 2"
    # js="var q=document.body.scrollTop=2000"
    # driver.execute_script(js)

    print "结束下拉"
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source)
    title_box_list = soup.find_all(class_='title-box')
    for title_box in title_box_list:
        print title_box

    #关闭浏览器
    driver.close()

def get_toutiao_url(class_name='news_essay'):
    current_time = int(time.time())
    # current_time = '1488925203'
    class_name = 'news_military'
    article_url_list = []
    # https://www.toutiao.com/api/pc/feed/?category=news_essay&utm_source=toutiao&widen=1&max_behot_time=1488884110&max_behot_time_tmp=1488884110&tadrequire=true
    # url = 'https://www.toutiao.com/api/pc/feed/?category=' + class_name + '&utm_source=toutiao&widen=1&max_behot_time=' + str(current_time) + '&max_behot_time_tmp=' + str(current_time)
    # url = 'https://www.toutiao.com/api/pc/feed/?category=news_military&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&'
    # url = 'https://www.toutiao.com/api/pc/feed/?category=news_military&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1C5280B3F1760D&cp=58BFB736B0DDEE1'
    # url = 'https://www.toutiao.com/api/pc/feed/?category=news_military&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1F5B8CB0F060FE&cp=58BFC6E0CF2E8E1'
    # url = 'https://www.toutiao.com/api/pc/feed/?category=news_military&utm_source=toutiao&widen=1&max_behot_time=1488925203&max_behot_time_tmp=1488925203&tadrequire=true&as=A1D5F86BCF37741&cp=58BF878734818E1'
    # url = 'https://www.toutiao.com/api/pc/feed/?category=news_military&utm_source=toutiao&widen=1&max_behot_time=1488910503&max_behot_time_tmp=1488910503&tadrequire=true&as=A14578CBCF677FD&cp=58BF7747DFAD0E1'
    url = 'https://www.toutiao.com/api/pc/feed/?category=news_military&utm_source=toutiao&widen=1&max_behot_time=1488943512&max_behot_time_tmp=1488943512&tadrequire=true&as=A175E84B0F47FD9&cp=58BF47AF5D996E1'
    # url = 'https://www.toutiao.com/api/pc/feed/?category=news_military&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A13558DBEF079C0&cp=58BFF7C9AC008E1'
    print url
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
    # response = requests.get(url=url, headers=headers, data=body)
    response = requests.get(url=url)
    response_dict = response.text
    print response_dict
    json_dict = simplejson.loads(response_dict.encode('utf-8'))
    print type(json_dict)
    for cloumn in json_dict['data']:
        print cloumn
        print cloumn['title']
        print cloumn['source_url']
        print type(cloumn['source_url'])
        print "----"
        if '/group/' in cloumn['source_url']:
            article_url_list.append(cloumn['source_url'])
    return article_url_list

def get_toutiao_article(article_url_list):

    for sub_url in article_url_list:
        # time.sleep(2)
        print 'sub_url',sub_url
        url = 'http://www.toutiao.com' + str(sub_url)
        print url
        response = requests.get(url,headers=headers)
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
        # print "content:  ",content_all

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

        # return title,src,time,keyword,content


if __name__ == '__main__':
    test_ajax()
    # test_pic()
    # test_url()
    # test_request()
    # article_url_list = get_toutiao_url()
    get_toutiao_article(article_url_list)