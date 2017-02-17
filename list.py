#!/usr/bin/env python
# coding=UTF-8

a = [23 ,35, 1, -3434, 432525,243]
a.insert(0,10)
#a.append(45)
print a
a.remove(35)
print a
a.reverse()
print a

b = a.pop(0)
print b

squares = []
for x in range(10):
    squares.append(x**2)
print squares



def compare():
    listA = ['address1', 'address2', 'address3', 'address4', 'address5']
    listB = ['address1', 'address5', 'address3']
    newList = []
    # 对比两个列表中的值，小表的值在大表中仅出现一次为True
    newList = [(x, y) for x in listB for y in listA if x == y]
    if newList.__len__() == listB.__len__():
        print "True"
    else:
        print "False"

if __name__ == "__main__":
    compare()

