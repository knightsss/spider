#coding:utf-8
__author__ = 'shifeixiang'
import os
import json
import requests
import re
import os.path
import time

import urllib2
import urllib

header_data={'Accept':'*/*',
    'Accept-Encoding':'gzip,deflate,sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Length':'108',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
    ,'Host':'www.zhihu.com'
    ,'Origin':'http://www.zhihu.com'
    ,'Referer':'http://www.zhihu.com/'
    ,'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'
    ,'X-Requested-With':'XMLHttpRequest'
    }

zhihu_url = 'http://www.zhihu.com'
login_url = zhihu_url+'/login/email'
captcha_url = zhihu_url+'/captcha.gif?r='
test_url = 'https://www.zhihu.com/people/wang-han-53/followers'

class Login():
    def __init__(self):
        global session
        self.cookie_login()

    def cookie_login(self):
        global session
        session = requests.session()
        if os.path.exists('cookie.txt'):
            print "cookie is exists"
            self.read_cookie()
        else:
            self.login()
    def read_cookie(self):
        with open('cookie.txt') as f:
            cookie = json.load(f)
            session.cookies.update(cookie)

    def login(self):
        global session     #定义全局变量，存放requests.seesion,创建一个会话
        global header_data  #头数据
        global xsrf         #xsrf数据
        global email
        global password
        global test_url
        r = session.get('http://www.zhihu.com')              #调用get方法 得到Response的对象
        self.xsrf = re.findall('xsrf(.*)',r.text)[0][8:42]      #在html中通过正则表达式获取参数
        self.email = '1251314160@qq.com'
        self.password = 'sfx918'
        self.save_captcha()
        print "请输入验证码--保存在/python_reptile/zhihu/login目录下"
        self.captcha = raw_input()
        login_data = {'xsrf':self.xsrf, 'email':self.email, 'password':self.password, 'captcha':self.captcha}   #登录数据
        response = session.post(login_url, data=login_data, headers=header_data)      #post请求
        j = response.json()     #获取response的json值
        if(j['r']==0):
            print "登陆成功"
            self.save_cookie()
        else :
            print "登陆失败"
    def save_cookie(self):
        global session

        with open ('cookie.txt','w') as f:
            json.dump(session.cookies.get_dict(),f)

    def save_captcha(self):
        global captcha_url
        r = session.get(captcha_url+str(int(time.time()*1000)))
        with open('captcha.jpg','wb') as f:
            f.write(r.content)

    def test_login(self):
        global session
        print "html is :   "
        response = session.get(test_url)
        print response.content

    def test_no_login(self):
        request = urllib2.Request(test_url)
        response = urllib2.urlopen(request)
        print response.read()
    def get_html(self,url):
        global session
        print "html is : ",url
        params = {
            'method':next,
            'params':{'offset':20}
        }
        #response = session.get(url)
        response = session.post(url,data = params,headers=header_data)
        print response.text
        items = re.findall('<a .*? href="https://www.zhihu.com/people/.*?" class="zg-link" .*?>(.*?)</a>',response.text)
        for item in items:
            print item
        #print response.content

def main():
    login = Login()
    #login.test_no_login()
    login.test_login()
    #login.get_html(test_url)

if __name__ == '__main__':
    main()

