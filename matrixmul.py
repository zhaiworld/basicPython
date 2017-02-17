#!/usr/bin/env python
# coding=UTF-8

from __future__ import print_function
#计算两个矩阵的乘积


n = int(input("Enter the value of n:"))
print ("Enter the value of the Matrix A")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])

print ("Enter the value of the Matrix B")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])

c = []
for i in range(n):
    c.append([a[i][j]*b[j][i] for j in range(n)])
print ("After matrix multiplication")
print ("-"* 7 * n)

for x in c:
    for y in x:
        print (str(y).rjust(5), end = ' ')
    print ()
print ("-"* 7 * n)