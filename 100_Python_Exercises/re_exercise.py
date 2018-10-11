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

###############################
#           No.5              #
###############################
# Q: 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
# 然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
def reverse():
    res = []
    while True:
        for i in range(3):
            num = int(raw_input('please insert a num: '))
            res.append(num)
    
        return sorted(res)

print(reverse())

###############################
#           No.6              #
###############################
'''题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

在数学上，费波那契数列是以递归的方法来定义：'''

def print_fib(n):
    # 0、1、1、2、3、5、8、13、21、34、……    
    fiblist = [1, 1]
    if n <= 1:
        return [1]
    elif n == 2:
        return fiblist
    
    for i in range(2,n):
        fiblist.append(fiblist[-1] + fiblist[-2])
    return fiblist
    
print print_fib(9)


def get_fib(n):
    a, b = 1, 1
    for i in range(2,n):
        a, b = a+b, a
    return a

def re_fib(n):
    if n < 3:
        return 1
    else:
        return re_fib(n-1) + re_fib(n-2)

print re_fib(9)


###############################
#           No.7              #
###############################
'''
题目：将一个列表的数据复制到另一个列表中。

程序分析：使用列表[:]。'''
def copy(a):
    return a[:]

print(copy([1,2,3,4,5,6]))


###############################
#           No.8              #
###############################
'''
题目：输出 9*9 乘法口诀表。

程序分析：分行与列考虑，共9行9列，i控制行，j控制列。'''
for i in range(1,10):
    print
    for j in range(1,i+1):
        print('%d*%d=%d' % (i, j, i*j))
        

###############################
#           No.9              #
###############################
    
'''题目：暂停一秒输出。

程序分析：使用 time 模块的 sleep() 函数。'''
import time
def print_n():
    for i in range(3):
        print(i)
        print
        time.sleep(1)

print_n()

###############################
#           No.11             #
###############################
    
'''题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

程序分析：兔子的规律为数列1,1,2,3,5,8,13,21.... '''
# decompose: f1, f2, f3 and how their value change by each month
def get_rab(n_month):
    if n_month < 3:
        return 1
    f1, f2 = 1, 1
    for i in range(n_month-1):
        f1, f2 = f2, f1+f2
    return f1
      
get_rab(7)


###############################
#           No.12             #
###############################
    
'''题目：判断101-200之间有多少个素数，并输出所有素数。

程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，
如果能被整除，则表明此数不是素数，反之是素数。 '''

def prime():
    total = 0
    for num in range(101, 201):
        for divided in range(2, num):
            if num % divided == 0:
                # not prime num
                break
        # mistake made here
        
        else:
            print num
            total += 1
    return total
        
print(prime())
 
###############################
#           No.13             #
###############################
    
'''题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。''' 

def find():
    for num in range(100,1000):
        hun = num / 100
        tens = num % 100 / 10
        units = num % 10
        if num == hun*hun*hun + tens*tens*tens + units*units*units:
            print num
            
find()

###############################
#           No.14             #
###############################
    
'''题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,
重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。'''
def factor(num):
    res = []
    while num > 1:
        for i in range(2,num+1):
            if num%i == 0:
                # a factor
                num /= i
                res.append(i)
                break
    return res
print(factor(190))


###############################
#           No.15             #
###############################
'''
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，
        60-89分之间的用B表示，
        60分以下的用C表示。

程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。'''
def cut(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 60:
        return 'B'
    else:
        return 'C'
cut(89)

###############################
#           No.16             #
###############################
    
'''题目：输出指定格式的日期。

程序分析：使用 datetime 模块。'''
import time, datetime
print datetime.date.today().strftime('%d-%m-%Y')
bd = datetime.date(1999,9,8)
next_d = bd + datetime.timedelta(1)
print next_d

###############################
#           No.17             #
###############################
    
'''题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。'''
def analysis(string):
    alpha, space, digit, other = 0, 0, 0, 0
    for rune in string:
        if rune.isalpha():
            alpha += 1
        elif rune.isdigit():
            digit += 1
        elif rune.isspace():
            space += 1
        else:
            other += 1
    print('%d letters, %d digits, %d spaces, %d others' % (
            alpha, digit, space, other))

analysis('Today is 10 10 2018.')

###############################
#           No.18             #
###############################
    
'''题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

程序分析：关键是计算出每一项的值。
'''
# key format the string








