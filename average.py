#!/usr/bin/env/ python
# coding=UTF-8

#求N个数的平均值
N = 4
#求和
sumresult = 0
#计数器
count = 0

while count < N:
    number = float(input("enter the number"))
    sumresult = sumresult + number
    count = count + 1

average = sumresult / N
print ("N numbers sum = {}".format(sumresult))
print ("N numbers average = {:.2f}".format(average))