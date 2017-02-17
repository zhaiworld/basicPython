#!/usr/bin/env python
# coding=UTF-8

courses = ['english','chinese','math']
dict = {}#用来存储数据的字典变量


#录入学生数量
studentCount = int(input("enter the number of students"))

for i in range(studentCount):
    name = input("enter the name of NO.{}".format(i + 1))
    marks = []
    for x in courses:
        marks.append(int(input("enter marks of {}".format(x))))
    dict[name] = marks

for x,y in dict.items():
    total = sum(y)
    print ("student {}'s total marks {}".format(x,total))
    if total < 120:
        print (x,"failed :(")
    else:
        print (x,"passed :)")