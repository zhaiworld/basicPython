#!/usr/bin/env python
# coding=UTF-8
from __future__ import print_function

def generator_function():
    for i in range(10):
        yield i

for item in generator_function():
    print (item)

#计算斐波那契数列的生成器
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

for x in fibon(10):
    print (x)