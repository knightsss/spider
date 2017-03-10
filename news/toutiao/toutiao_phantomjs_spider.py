#coding=utf-8
__author__ = 'shifeixiang'

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
import MySQLdb
import redis

def get_webdriver():
    driver = webdriver.PhantomJS('E:\\phantomjs\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs')
    return driver

def get_url_args(driver,toutiao_class):
    # chrome_driver = os.path.abspath(r"D:\云盘\360云\360云盘\我的自动双向同步文件夹\01-PersonalInfo\DataGuru\12-软件自动化测试Selenium2\1-课程\练习代码_Python版本\Selenium_python\Files\chromedriver.exe")
    # os.environ["webdriver.chrome.driver"] = chrome_driver
    # driver = webdriver.Chrome(chrome_driver)

    # chrome_driver = os.path.abspath(r"F:\auto_windows\atom-windows\Atom\new_chrome\chromedriver.exe")   #谷歌浏览器位置
    # os.environ["webdriver.chrome.driver"] = chrome_driver            #设置环境变量
    # driver = webdriver.Chrome(chrome_driver)             #webdriver获取

    # driver = webdriver.Firefox()
    #webdriver中的PhantomJS方法可以打开一个我们下载的静默浏览器。
    #输入executable_path为当前文件夹下的phantomjs.exe以启动浏览器
    # driver =webdriver.PhantomJS(executable_path="phantomjs.exe")

    #使用浏览器请求页面
    # driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
    url = "https://www.toutiao.com/" + str(toutiao_class) + "/"
    print "url",url
    try:
        driver.get(url)
    except:
        return 0
    #加载3秒，等待所有数据加载完毕
    time.sleep(3)
    #通过id来定位元素，
    #.text获取元素的文本数据
    # print driver.find_element_by_id('content').text
    #模拟滚动条下拉5次
    pull_times = 3
    for i in range(pull_times):
        print "pull ",str(i)
        js="var q=document.body.scrollTop=" + str((i+1)*1000)
        driver.execute_script(js)
        time.sleep(3)
    print "结束下拉"
    time.sleep(3)
    # print driver.page_source
    soup = BeautifulSoup(driver.page_source)
    url_args_list = []
    title_box_list = soup.find_all(class_='title-box')
    for title_box in title_box_list:
        print title_box
        print type(title_box.a['href'])
        url_args = title_box.a['href']
        if '/group/' in url_args:
            url_args_list.append(url_args)
    #关闭浏览器
    # driver.close()
    return url_args_list

def get_toutiao_article(article_url_list):

    for sub_url in article_url_list:
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

def connect_db():
    try:
        mysql_conn = MySQLdb.connect("localhost","root","123456","db_news")
    except:
        print "connect mysql error"
        return None
    return mysql_conn

def insert_mysql_article(mysql_conn,tmp):
    mysql_cursor = mysql_conn.cursor()
    sql = "insert into t_news_toutiao_article(qq, friend_qq) values(%s, %s)"
    # tmp结构 tmp = (('00', '0000'), ('10', '111'))
    mysql_cursor.executemany(sql, tmp)
    mysql_conn.commit()
    return 0

#连接redis
def redis_connect():
    #带密码连接
    # r = redis.StrictRedis(host='localhost', port=6379, password='npq8pprjxnppn477xssn')
    try:
        redis_conn = redis.Redis(host='192.168.15.111',port=6379,db=0)
        # redis_conn = redis.StrictRedis(host='192.168.15.111', port=6379, password='npq8pprjxnppn477xssn',db=0)
    except:
        print "connect redis error"
        redis_conn = 0
    return redis_conn

#出队
def pop_redis_list(redis_conn,redis_list_name):
    try:
        qq = redis_conn.lpop(redis_list_name)
        # print "pop ok"
    except:
        # redis_conn = redis_connect()
        print "pop faild"
        qq = None
    return qq


#入队
###redis连接 redis list名字 value
def push_redis_list_tmp(redis_conn,redis_list_name,value):
    try:
        redis_conn.rpush(redis_list_name,value)
    except:
        redis_conn = redis_connect()


def get_toutiao_class():
    toutiao_class = []
    with open('toutiao_class.txt','r') as f:
        lines = f.readlines();
        for line in lines:
            line = line.strip('\n')
            toutiao_class.append(line)
    return toutiao_class

if __name__ == '__main__':
    toutiao_class_list = get_toutiao_class()
    #连接redis
    redis_conn = redis_connect()
    #获取driver
    driver = get_webdriver()
    #设置头条类别
    # toutiao_class = 'news_military'
    #获取url的参数    /group/1234567
    for toutiao_class in toutiao_class_list:
        url_args_list = get_url_args(driver,toutiao_class)
        #入临时消息队列
        if url_args_list == 0:
            break
        else:
            for url in url_args_list:
                push_redis_list_tmp(redis_conn,'n_t_test_tmp',url)
    driver.close()
    # get_toutiao_article(url_args_list)
