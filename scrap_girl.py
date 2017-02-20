#!/usr/bin/env python
# coding=UTF-8

#通过urllib2模块下载网络内容
import urllib,urllib2,gevent
import re,time
from gevent import monkey

monkey.patch_all()

def geturllist(url):
    url_list =[]
    print url
    s = urllib2.urlopen(url)
    text = s.read()
    #正则匹配，匹配其中的图片
    html = re.search(r'<ol.*</ol>',text,re.S)
    urlre = re.finditer(r'<p>.*<img src="(.+?)jpg".*</p>',text,re.I)
    for picurl in urlre:
        if 'http://' in picurl.group(1):
            url = picurl.group(1).strip('//')+str("jpg")
        else:
            url = str("http://") + picurl.group(1).strip('//') + str("jpg")
        url_list.append(url)
    return url_list

def download(down_url):
    name = str(time.time())[:-3]+"_"+re.sub('.+?/','',down_url)
    print name
    urllib.urlretrieve(down_url,"C:\\temp\\scrap_girl\\"+name)

def getpageurl():
    page_list=[]
    #循环获得列表页
    for page in range(120):
        url = "http://jiandan.net/ooxx/page-"+str(page)+"#comments"
        #把生成的url加入到列表中
        page_list.append(url)
    #print page_list
    return page_list

if __name__ =='__main__':
    jobs = []
    pageurl = getpageurl()[::-1]
    #进行图片下载
    for i in pageurl:
        for downurl in geturllist(i):
            jobs.append(gevent.spawn(download,downurl))
        gevent.joinall(jobs)