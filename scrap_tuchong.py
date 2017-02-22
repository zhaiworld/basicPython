#!/usr/bin/env python
# coding=UTF-8
from __future__ import print_function
import urllib,re,gevent
from gevent import monkey

monkey.patch_all()
# 生成URL库
# 定位figures-wrapper，找出图片url库
#下载到本地，以主题为文件夹保存

def getpageid(url):
    pagelist = [url]
    res = urllib.urlopen(url)
    s = res.read()
    #通过re获取pagebar，知道共有几页数据
    pagebar = re.search(r'<div class="pagebar">(.*)<footer',s,re.S)
    pageiditer = re.finditer(r'<a href="(.+?)">',pagebar.group(1),re.I)
    nexturl = url
    for page in pageiditer:
        nexturl = url + page.group(1)
        yield nexturl


def getidwapper(url):#通过根链接，获得链接库
    id_list = [url]
    for x in getpageid(url):
        id_list.append(x)
    return id_list

def getsiteidurl(idlist):
    siteidurllist = []
    for id_url in idlist:
        #print (idlist)
        #print (id_url)
        res = urllib.urlopen(id_url)
        s = res.read()
        sitegroup = re.search(r'<div class="post-row"(.+?)<div class="pagebar">',s,re.S)
        siteidurliters = re.finditer(r'<a data-site-id=.+?href="(.+?)"',sitegroup.group(),re.I)
        for i in siteidurliters:
            #print (i.group(1))
            siteidurllist.append(i.group(1))
    print (len(siteidurllist))

    for i in siteidurllist:
        resp = urllib.urlopen(i)
        text = resp.read()
        piciters = re.finditer(r'<img src="(.+?)".*?class="img-responsive copyright-contextmenu"', text, re.I)
        for x in piciters:
            pic_url = x.group(1)
            yield pic_url

def downloads(idwapperls):
    jobs = []
    for pic in getsiteidurl(idwapperls):
        jobs.append(gevent.spawn(down, pic))
    gevent.joinall(jobs)

def down(picurl):
    name = re.sub('.+?/','',picurl)
    urllib.urlretrieve(picurl, 'C:\\temp\\scrap_girl\\'+name)

if __name__ == "__main__":
    idurl="https://tuchong.com/tags/%E5%9B%BE%E8%99%AB%E4%B8%80%E5%91%A8%E7%B2%BE%E9%80%89/"
    idwapperlist = []
    idwapperlist = getidwapper(idurl)
    downloads(idwapperlist)

