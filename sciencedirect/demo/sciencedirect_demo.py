#coding=utf-8
__author__ = 'shifeixiang'

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os


def get_webdriver():
    #谷歌浏览器
    # chrome_driver = os.path.abspath(r"F:\auto_windows\atom-windows\Atom\new_chrome\chromedriver.exe")   #谷歌浏览器位置
    # os.environ["webdriver.chrome.driver"] = chrome_driver            #设置环境变量
    # driver = webdriver.Chrome(chrome_driver)             #webdriver获取

    #phantomjs
    driver = webdriver.PhantomJS('E:\\phantomjs\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs')
    return driver

def get_url_args(driver,url):
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
    # url = "https://www.toutiao.com/" + str(toutiao_class) + "/"
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
    pull_times = 1
    for i in range(pull_times):
        print "pull ",str(i)
        js="var q=document.body.scrollTop=" + str((i+1)*1000)
        driver.execute_script(js)
        time.sleep(3)
    print "结束下拉"
    time.sleep(3)
    # print driver.page_source.encode('utf-8')
    soup = BeautifulSoup(driver.page_source)
    url_args_list = []
    browseimpBrowseRow_list = soup.find_all(class_='browseimpBrowseRow')
    for browseimpBrowseRow in browseimpBrowseRow_list:
        if 'www.sciencedirect.com/science/journal/' in browseimpBrowseRow.a['href']:
            url_args_list.append(browseimpBrowseRow.a['href'])
        elif '/science/journal/' in browseimpBrowseRow.a['href']:
            url_args_list.append('www.sciencedirect.com' + browseimpBrowseRow.a['href'])

    # title_box_list = soup.find_all(class_='title-box')
    # for title_box in title_box_list:
    #     print title_box
    #     print type(title_box.a['href'])
    #     url_args = title_box.a['href']
    #     if '/group/' in url_args:
    #         url_args_list.append(url_args)
    #关闭浏览器
    # driver.close()
    return url_args_list

import urllib2

def get_periodical(driver,url):
    print '==='

    # response = requests.get(url)
    # print response.text.encode('utf-8')
    # request = urllib2.Request(url)
    # response = urllib2.urlopen(request)
    driver.get(url)
    # print driver.page_source
    time.sleep(3)
    print type(driver.find_element_by_class_name('author-name'))
    authors = driver.find_elements_by_class_name('author-name')
    # driver.find_elements_by_class_name()
    for author in authors:
        print "type(author) ",type(author)
        author.click()
        time.sleep(3)
        current_page = driver.page_source
        soup  = BeautifulSoup(current_page)
        print soup.find(class_='WorkspaceAuthor').find(class_='author-name').string
        print soup.find(class_='author-affiliation').string
        print soup.find(class_='author-emails').a['href'][7:]
        if soup.find(class_='author-correspondences') != None:
            for x in soup.find(class_='author-correspondences').stripped_strings:
                print x
        time.sleep(1)
    time.sleep(3)
    driver.find_element_by_class_name('WorkspaceAuthor')
    # print driver.page_source
    # soup  = BeautifulSoup(driver.page_source)
    # WorkspaceAuthor = soup.find(class_='WorkspaceAuthor')

if __name__ == '__main__':
    # url = 'http://www.sciencedirect.com/science/journals/'
    driver = get_webdriver()
    # url_args_list = get_url_args(driver,url)
    # print url_args_list
    print "---"
    # print url_args_list[0]

    url = 'http://www.sciencedirect.com/science/article/pii/S2212671614001024'
    # url = 'http://www.baidu.com'
    get_periodical(driver,url)

    driver.close()