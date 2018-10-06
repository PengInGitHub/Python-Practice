#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""
# resource
# http://www.runoob.com/python/python-exercise-example1.html
###############################
#           No.1              #
###############################
# Q: 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# Analysis: 可填在百位、十位、个位的数字都是1、2、3、4。
# 组成所有的排列后再去 掉不满足条件的排列。
'''
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                print i, j, k
                


profits = [1000000, 600000, 400000, 200000, 100000, 0]
rates = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
profit_input = int(raw_input("your profit is: "))
commission = 0

for idx in range(0, len(profits)):
    # profits above current level
    if profit_input > profits[idx]:
        # calculate commissons for this surplus
        commission += (profit_input - profits[idx]) * rates[idx]
        # deduct profit_input's surplus to profits at current level
        profit_input = profits[idx]
print "{:,}".format(int(commission))

# x is an int
# x + 100 = n^2, x + 100 + 168 = m^2
# what value is x ?

# m^2 - n^2 = 168
# (m+n)(m-n) = 168
# i = m+n, j = m-n, i and j are 



year = int(raw_input("input the year: "))
month = int(raw_input("input the month: "))
day = int(raw_input("input the day: "))

month_days = [0, 31, 58, 90, 120, 151, 181, 212, 243, 273, 304, 334]
if 0<month<=12 and 0<day<=31:
    days =  month_days[month-1] + day
    print days
else:
    print 'invalid input in year, month or day'
 
nums = []
for i in range(3):
    nums.append(int(raw_input('input an int: ')))
print sorted(nums)


# fib
# 0、1、1、2、3、5、8、13、21、34、……
def f(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a 

def flist(n):
    flist = [1, 1]
    if n == 1:
        return [1]
    if n == 2:
        return flist
    for i in range(2, n-1):
        flist.append(flist[-1]+flist[-2])
    
    return flist
print flist(8)
'''
# products matrix
for i in range(1,10):
    print
    for j in range(1,i+1):
       print "%d*%d=%d" % (i, j, i*j) 









