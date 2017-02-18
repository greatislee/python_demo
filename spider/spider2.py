#!/usr/bin/env python
# coding=utf-8

import urllib2

url = "http://www.dota2.com"

user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"

header= {"User-Agent": user_agent}

request = urllib2.Request(url,headers=header)


#发送url请求
response = urllib2.urlopen(request)


#得到返回的结果

caoliu_text  = response.read()


print caoliu_text
