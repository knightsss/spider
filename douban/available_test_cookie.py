#coding=utf-8
import urllib2
import cookielib
import re
import urllib

def print_cookie():
    #声明一个CookieJar对象实例来保存cookie
    cookie = cookielib.CookieJar()
    #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler=urllib2.HTTPCookieProcessor(cookie)
    #通过handler来构建opener
    opener = urllib2.build_opener(handler)
    #此处的open方法同urllib2的urlopen方法，也可以传入request
    response = opener.open('https://www.douban.com/accounts/login')
    for item in cookie:
        print 'Name = '+item.name
        print 'Value = '+item.value

def save_cookie():
    #设置保存cookie的文件，同级目录下的cookie.txt
    filename = 'cookie.txt'
    #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookielib.MozillaCookieJar(filename)
    #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    #通过handler来构建opener
    opener = urllib2.build_opener(handler)
    #创建一个请求，原理同urllib2的urlopen
    response = opener.open("http://www.baidu.com")
    #保存cookie到文件
    cookie.save(ignore_discard=True, ignore_expires=True)

def load_cookie():
    #创建MozillaCookieJar实例对象
    cookie = cookielib.MozillaCookieJar()
    #从文件中读取cookie内容到变量
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    #创建请求的request
    req = urllib2.Request("http://www.baidu.com")
    #利用urllib2的build_opener方法创建一个opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    print response.read()

def save_douban_cookie():
    login_data = {
            'source':'None',
            'redir':"https://www.douban.com/doumail/",
            'form_email':'1251314160@qq.com',
            'form_password':'sfx19900918',
            'login':"登录",
            'remember': "on"
    }
    login_url = "https://www.douban.com/accounts/login"
    #设置保存cookie的文件，同级目录下的cookie.txt
    filename = 'douban_cookie.txt'
    #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookielib.MozillaCookieJar(filename)
    #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    #通过handler来构建opener
    opener = urllib2.build_opener(handler)
    #创建一个请求，原理同urllib2的urlopen
    #验证码标志，如果没有，则不发送很验证码相关的信息
    captcha_flag = 1
    if 1:
        response = opener.open(login_url)      #获取登陆界面的返回页
        html = response.read()
        try:
            pattern = re.compile('<img id="captcha_image" src="(.*?)" alt="captcha" class="captcha_image"/>', re.S)   #获取验证码的链接地址
            captcha_url_set = re.findall(pattern,html)
            captcha_url = captcha_url_set[0]
        except:
            print u"链接中没有验证码！"
            captcha_flag = 0
            # self.login()
        if captcha_flag:
            pattern2 = re.compile('<input type="hidden" name="captcha-id" value="(.*?)"/>', re.S)         #获取captcha-id的值
            captcha_id_set = re.findall(pattern2,html)
            captcha_id = captcha_id_set[0]

            print "The captcha_image link is %s" %captcha_url
            # self.save_captcha(captcha_url)
            print u"请输入验证码--点击链接查看"
            captcha_solution = raw_input()
            print captcha_solution
            login_data["captcha-solution"] = captcha_solution
            login_data["captcha-id"] = captcha_id
        else:
            pass

        r = opener.open(login_url,urllib.urlencode(login_data))
        print r.geturl()

        if r.geturl() == "http://www.douban.com/" or  r.geturl() == "https://www.douban.com/doumail/":
            print "login success"
            group = opener.open('https://www.douban.com/group/explore')
            group_html =  group.read()
            print group_html
            cookie.save(ignore_discard=True, ignore_expires=True)
            # cookie.save(ignore_discard=True, ignore_expires=True)
            # self.cookie.save()
        else :
            return False
    else:
        pass

def load_douban_cookie():
    #创建MozillaCookieJar实例对象
    cookie = cookielib.MozillaCookieJar()
    #从文件中读取cookie内容到变量
    cookie.load('douban_cookie.txt', ignore_discard=True, ignore_expires=True)
    #创建请求的request
    req = urllib2.Request("https://www.douban.com/group/explore")
    #利用urllib2的build_opener方法创建一个opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    print response.read()

if __name__ == '__main__':
    save_douban_cookie()
    load_douban_cookie()
