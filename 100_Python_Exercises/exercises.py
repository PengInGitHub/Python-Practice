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

def get_results():
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i != k and i != j and k!= j:
                    print i, j, k

'''if __name__ == '__main__':
    get_results()'''


###############################
#           No.2              #
###############################
# Q: 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，
# 低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，
# 高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，
# 高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

# Analysis: 请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。

def calculate_commission():
    profits = [1000000, 600000, 400000, 200000, 100000, 0]
    rates = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    commission = 0
    
    while True:
        try:
            net_profit = int(raw_input('Your profit is: '))
            for idx in range(0, len(profits)):
                if net_profit > profits[idx]:
                    commission += (net_profit-profits[idx])*rates[idx]
                    net_profit = profits[idx]
            print('\nYour commission is: ' + "{:,}".format(commission))
            return
            
            
        except(SyntaxError, ValueError):
            print('Please input a number.')
            continue
'''
if __name__ == '__main__':
    calculate_commission()'''


###############################
#           No.3              #
###############################
# Q: 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

''' 程序分析：
    
    假设该数为 x。
    
    1、则：x + 100 = n^2, x + 100 + 168 = m^2
    
    2、计算等式：m^2 - n^2 = (m + n)(m - n) = 168
    
    3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
    
    4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
    
    5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
    
    6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
    
    7、接下来将 i 的所有数字循环计算即可。'''

def calculate_int():
    res = []
    for i in range(1, 168/2+1):
        if 168 % i == 0:
            j = 168 / i
            # i and j are all even numbers
            if i > j and (i+j) % 2 == 0 and (i-j) % 2 == 0:
                m = (i + j) / 2
                n = (i - j) / 2
                x = n*n - 100
                print x
        
'''if __name__ == '__main__':
    calculate_int()   '''         

###############################
#           No.4              #
###############################
# Q: 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天,
# 特殊情况，闰年且输入月份大于2时需考虑多加一天：

def get_nth_day():
    while True:
        try:
            year = int(raw_input('year: '))
            month = int(raw_input('month: '))
            day = int(raw_input('day: '))
            
            month_days = [0, 31, 59, 90, 120, 151,
                          181, 212, 243, 273, 304, 334]
            
            if 0<month<=12:
                days_sum = month_days[month]
            else:
                print('Month is not approprivate.')
                continue
            if 0<day<=31:
                days_sum += day
            else:
                print('Day is not appropriate.')
                continue
            days_sum + check_leap_year(year, month)
            print('\nIt is the %dth day in the year.'%days_sum)
            return
            
        
        except(SyntaxError, ValueError):
            print('please check the your input is an integer')
            continue

def check_leap_year(year, month):
    if 0<year:
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            if month > 2:
                return 1
    return 0
        
'''        
if __name__ == '__main__':
    get_nth_day()'''





































