#coding:utf-8
#已提交到git
#登陆次数过多时禁止访问
__author__ = 'shifeixiang'
import urllib2
import urllib
import requests
import re
import sys
import cookielib
import json
import os.path
import time
import HTMLParser

login_url='https://www.douban.com/accounts/login'
test_url = 'http://www.douban.com/people/knight_sfx/'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER'}
header1 = {
    'Host':'www.douban.com',
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
    'Accpet': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding':'gzip, deflate',
    'Referer':'http://www.douban.com/',
    'Connection':'keep-alive',
    'Content-Length':'138',
    'Content-Type':'application/x-www-form-urlencoded',
}
header2 = { 'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"}

class Login():
    def __init__(self):
        global session
        session = requests.Session()     #创建会话

        self.source = 'None'
        self.redir = "https://www.douban.com/doumail/"
        self.form_email = '1251314160@qq.com'
        self.form_password = 'sfx19900918'
        self.captcha_id = None
        self.captcha_solution = None
        self.login_value = "登录"

        #构造请求的数据
        self.login_data = {
            'source':self.source,
            'redir':self.redir,
            'form_email':self.form_email,
            'form_password':self.form_password,
            'login':self.login_value,
            # "remember": "on"
        }                           #login_data所需参数可以通过火狐浏览器登录时查看源码(F12)--网络--login的POST请求，查看参数表单数据

        self.cookie_file = 'cookie_save.txt'
        self.cookie = cookielib.LWPCookieJar(self.cookie_file)
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        #self.cookie = cookielib.LWPCookieJar()  #声明一个CookieJar对象实例来保存cookie--<LWPCookieJar[]> <type 'instance'>
        #self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie)) #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器--<urllib2.HTTPCookieProcessor instance at 0x0000000002774E88> <type 'instance'>
        #urlopen方法使用的是默认的opener来处理问题，基本的urlopen()函数不支持验证、cookie或其他的HTTP高级功能。
        # 要支持这些功能，必须使用build_opener()函数来创建自己的自定义Opener对象。--<urllib2.OpenerDirector instance at 0x0000000002774F08> <type 'instance'>
        self.load_cookie()
    def load_cookie(self):
        try :
            print "load cookie ..."
            self.cookie = cookielib.LWPCookieJar('cookie_save.txt')
            self.cookie.load(self.cookie_file)
        except:
            print "no the cookie txt"
            self.login()
            self.load_cookie()

    def login(self):
        #response = self.opener.open(login_url,urllib.urlencode(self.login_data))
        response = self.opener.open(login_url)      #获取登陆界面的返回页
        html = response.read()
        try:
            pattern = re.compile('<img id="captcha_image" src="(.*?)" alt="captcha" class="captcha_image"/>', re.S)   #获取验证码的链接地址
            captcha_url_set = re.findall(pattern,html)
            captcha_url = captcha_url_set[0]
        except:
            print u"链接中没有验证码！"
            # self.login()

        pattern2 = re.compile('<input type="hidden" name="captcha-id" value="(.*?)"/>', re.S)         #获取captcha-id的值
        captcha_id_set = re.findall(pattern2,html)
        self.captcha_id = captcha_id_set[0]

        print "The captcha_image link is %s" %captcha_url
        self.save_captcha(captcha_url)
        print u"请输入验证码--点击链接查看"
        self.captcha_solution = raw_input()
        print self.captcha_solution
        self.login_data["captcha-solution"] = self.captcha_solution
        self.login_data["captcha-id"] = self.captcha_id

        r = self.opener.open(login_url,urllib.urlencode(self.login_data))
        print r.geturl()

        if r.geturl() == "http://www.douban.com/" or  r.geturl() == "https://www.douban.com/doumail/":
            print "login success"
            group = self.opener.open('https://www.douban.com/group/explore')
            group_html =  group.read()
            print group_html
            self.cookie.save()
        else :
            return False
        return True
        # rr = self.opener.open(test_url)
        # html = rr.read()
        #print html

    def save_captcha(self,captcha_url):     #保存验证码到本地
        response = session.get(captcha_url)
        with open('douban_captcha.jpg','wb') as f:
            f.write(response.content)

    def my_request(self,url):
        page = self.opener.open(url)
        return page
def main():
    #创建登陆对象，第一次需要手动输入验证码，保存cookie，接下来根据cookies便可以访问
    login = Login()
    print "登陆成功"
    response = login.my_request('http://www.douban.com/people/knight_sfx/notes')
    html = response.read()
    pattern = re.compile('<div class="note-header-container">(.*?)</div>', re.S)
    #pattern = re.compile('<div class="article">.*?<div id=".*? class="note">(.*?)</div>.*?</div>', re.S)
    items = re.findall(pattern,html)
    print "结束"
    # group = login.my_request('https://www.douban.com/group/explore')
    # group_html =  group.read()
    # #print items
    # #for item in items:
    #     #print item
    # print group_html

def login():
    response = requests.get(login_url)
    html = response.content
    # print html
    try:
        pattern = re.compile('<img id="captcha_image" src="(.*?)" alt="captcha" class="captcha_image"/>', re.S)   #获取验证码的链接地址
        captcha_url_set = re.findall(pattern,html)
        captcha_url = captcha_url_set[0]
        print captcha_url
    except:
        print u"链接中没有验证码！"


if __name__ == "__main__":
    main()
    # login()

#参考douban_cookie_source

