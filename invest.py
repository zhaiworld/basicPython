#!/usr/bin/env python
# coding=UTF-8

#输入金额
amount = float(input("enter amount:"))
#输入利率
inrate = float(input("enter interest rate:"))
#输入期限
period = int(input("enter period:"))

value = 0
year = 1

while year<=period:
    value = amount +(inrate *amount)
    print ("year{} Rs.{:.2f}".format(year,value))
    amount = value
    year = year+1


