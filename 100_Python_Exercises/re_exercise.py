#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:34:34 2018

@author: pengchengliu
"""

###############################
#           No.1              #
###############################
# Q: 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# Analysis: 可填在百位、十位、个位的数字都是1、2、3、4。
# 组成所有的排列后再去 掉不满足条件的排列。
def cal():
    count = 0
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i!=k and j!=k and i!=j:
                    print(i,j,k)
                    count += 1
    return count

print(cal())


###############################
#           No.2              #
###############################
# Q: 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，
# 低于20万元时，低于10万元的部分按10%提成，
# 高于10万元的部分，可提成7.5%；20万到40万之间时，
# 高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，
# 高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

# Analysis: 请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。


def cal_commission():
    commission = 0.0
    profit_pool = [1000000.0, 600000.0, 400000.0, 200000.0, 100000.0, 0.0]
    comission_rates =  [0.01,    0.015,     0.03,     0.05,    0.075, 0.1]
    
    profit = int(raw_input('Your profit is: '))
    
    for idx in range(len(profit_pool)):
        # have higher profit than current level
        if profit > profit_pool[idx]:
            # get underlying profits
            commission += (profit - profit_pool[idx]) * comission_rates[idx]
            # made mistake here
            # profit -= profit_pool[idx]
            profit = profit_pool[idx]
    return commission

            
cal_commission()


###############################
#           No.3              #
###############################
''' Q: 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，
 请问该数是多少？
 x + 100 = n*n
 x + 100 + 168 = m*m
 (m+n)(m-n) = 168
 m + n = i, is an even num
 m - n = j, is an even num
 so m and n are both even num
 

 程序分析：
    
    假设该数为 x。
    
    1、则：x + 100 = n^2, x + 100 + 168 = m^2
    
    2、计算等式：m^2 - n^2 = (m + n)(m - n) = 168
    
    3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
    
    4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
    
    5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
    
    6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
    
    7、接下来将 i 的所有数字循环计算即可。'''



###############################
#           No.4              #
###############################
# Q: 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天,
# 特殊情况，闰年且输入月份大于2时需考虑多加一天：
    
def cal_day(year, month, day):
    month_days = [0,31, 59, 90, 120, 151,181,212,243,273,304,334]
    if 1<=month<=12:
        n_day = month_days[month-1]
    if 1 <= day <= 31:
        n_day += day
    # ignore leap year
    return n_day
        
cal_day(1998, 12, 31)






