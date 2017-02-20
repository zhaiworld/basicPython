#!/usr/bin/env python
# coding=UTF-8

import urllib
import urllib2


'''
urllib小练习
res = urllib.urlopen('http://www.baidu.com')
print res.getcode()

for line in res:
    print line
res.close()

'''

'''
urllib2小练习
'''

req = urllib2.Request('http://www.baidu.com')
res = urllib2.urlopen(req)
print res.code
print res.read()
res.close()

