#!/usr/bin/env python
# coding=utf-8

import urllib2

tieba_url  = "http://tieba.baidu.com/f?kw=dota2&ie=utf-8&pn=0"

#pn = 0 是第一页

#pn = 50 是第二页

#pn = 100 是第三页

#pn = 50 *(page -1)


#加载请求一个url页码
def load_page(url):

    user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
    header= {"User-Agent": user_agent}

    request = urllib2.Request(url, headers = header)

    #发送url请求
    response = urllib2.urlopen(request)
    #得到返回的数据
    html_text = response.read()

    return html_text

def write_file(filename,text):
    print "正在存储"+filename
    fp = open(filename,"w")
    fp.write(text)
    print "存储成功"+filename
    fp.close()

def tieba_spider(begin_page,end_page):

    for page in range(begin_page,end_page+1):
        print "开始存储第"+str(page)+"网页"

        #通过page封装url
        pn = 50 *(page - 1)
        temp_url = tieba_url+str(pn)

        #发送url请求 得到数据
        html_text = load_page(temp_url)

        filename = str(page)+".html"
        write_file(filename,html_text)


if __name__ == "__main__":
    begin_page = int (raw_input("请输入起始页码"))
    end_page = int (raw_input("请输入终止页码"))

    #开始爬
    tieba_spider(begin_page,end_page)

    #完毕
    print "done"



