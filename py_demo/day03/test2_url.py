#coding:utf-8

import urllib2

url = "http://www.baidu.com"

#模拟火狐浏览器
user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
header= {"User-Agent": user_agent}

request = urllib2.Request(url, headers = header)

#发送url请求
response = urllib2.urlopen(request)


#得到返回数据
html_text = response.read()

print html_text
