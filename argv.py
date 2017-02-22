#!/usr/bin/env python
# coding=UTF-8
from __future__ import print_function

def test_args(arg1, *argv):
    print ("first normal argument:",arg1)
    for i in argv:
        print ("other args through *argv:",i)

def kw_test(**kwargs):
    for key, value in kwargs.items():
        print ("{0} == {1}".format(key,value))

def test_argv_kwargs(arg1,arg2,arg3):
    print ('first:',arg1)
    print ('second:',arg2)
    print ('third:',arg3)

if __name__ =="__main__":
    #首先使用*args
    args = ("hello",3,9)
    test_argv_kwargs(*args)
    #再使用**kwargs
    kwargs = {'arg3':9,'arg2':3,'arg1':"hello"}
    test_argv_kwargs(**kwargs)

    kw_test(name="python")
    test_args('first','python','eggs','test')

