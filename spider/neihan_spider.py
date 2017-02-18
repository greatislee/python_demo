#!/usr/bin/env python
# coding=utf-8


class Spaider:
    '''
    爬虫类
    '''
    def __init__(self):
        #当前爬虫需要爬取的页码
        self.page = 1

    def load_page(self,url):
        '''加载某个页面 得到全部该页码源码'''
        user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
        header= {"User-Agent": user_agent}

        request = urllib2.Request(url, headers = header)

        #发送url请求
        response = urllib2.urlopen(request)
        #得到返回数据
        html_text = response.read()
        return  html_text

    def spider_one_page(self):
        '''
        爬取第page页，同时得到该页的全部段子的url列表
        '''
        if(self.page == 1):
            url = "http://www.neihan8.com/article/index.html"
        else:
            url = "http://www.neihan8.com/article/index_"+str(self.page)+".html"
            html_text = self.load_page(url)

            #得到全部的段子的url地址
            pattern = re.compile('<h3><a href="(.*?)"',re.S)

            dz_url_list = pattern.findall(html_text)

            print dz_url_list

            return dz_url_list

    def spider_dzurl_list(self,url_list):
        '''
        根据url_list 分别请求段子的网页，爬取段子的内容
        '''
        titles = []
        contents = []

        for url in url_list:
            dz_url = "http://www.neihan8.com"+url

            html_text = self.load_page(dz_url)

            #得到标题




    def doWork(self):
        '''
        爬虫的主业务方法
        '''
        while True:
            print "输入回车爬取下一页"
            print "输入exit退出"
            cmd = raw_input("请输入")
            if (cmd == 'exit'):
                break
        #开始爬去
        dz_url_list = self.spider_one_page()
        self.spider_dzurl_list(dz_url_list)
        #爬取该页完毕
        print "爬取" + str(self.page)+"完毕"
        self.page += 1



if __name__ == "__main__":

    sp = Spaider()

    sp.doWork()

