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

###############################
#           No.5              #
###############################
# Q: 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
# 然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。

def sort_num():
    l = []
    while True:
        # take 3 num
        try:
            for i in range(3):
                num = int(raw_input('input the %d integer: '%(i+1)))
                l.append(num)
            print('sorted numbers: ', sorted(l))
            return
          
        except(SyntaxError, ValueError):
            print('please check the your input is an integer')
            continue
    
'''if __name__ == '__main__':
    sort_num()'''


###############################
#           No.6              #
###############################
'''题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

在数学上，费波那契数列是以递归的方法来定义：'''
def fib(n):
    # 0、1、1、2、3、5、8、13、21、34、……
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a 

def fib_re(n):
    # 0、1、1、2、3、5、8、13、21、34、……
    if 0 < n < 3:
        return 1
    return fib_re(n-1) + fib_re(n-2)

def fib_list(n):
    fibs = [1, 1]
    if n == 1:
        return [1]
    if n == 2:
        return fibs
    for i in range(2,n):
        fibs.append(fibs[-1] + fibs[-2])
    
    return fibs

'''if __name__ == '__main__':
    print fib_list(9)'''


###############################
#           No.7              #
###############################
'''
题目：将一个列表的数据复制到另一个列表中。

程序分析：使用列表[:]。'''

# copy a list content to another
def copy_list():
    a = [1,2,2,3]
    b = a[:]
    return b

'''if __name__ == '__main__':
    print copy_list()'''


###############################
#           No.8              #
###############################
'''
题目：输出 9*9 乘法口诀表。

程序分析：分行与列考虑，共9行9列，i控制行，j控制列。'''

def mutiply_matrix():
    for i in range(1, 10):
        print
        for j in range(1, i+1):
            print("%d*%d=%d" % (i, j, i*j))


###############################
#           No.9              #
###############################
    
'''题目：暂停一秒输出。

程序分析：使用 time 模块的 sleep() 函数。'''

import time, datetime
def my_d():
    my_d = {'a':1, 'b':100, 'c':101}
    for key, value in dict.items(my_d):
        print key, value
        time.sleep(1) # pause for one second

def print_time():
    current = datetime.datetime.now()
    time.sleep(1)
    print current

if __name__ == '__main__':
    print_time()

###############################
#           No.12             #
###############################
    
'''题目：判断101-200之间有多少个素数，并输出所有素数。

程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，
如果能被整除，则表明此数不是素数，反之是素数。 '''

def find_prime(start=101, end=200):
    total = 0
    for i in range(start, end+1):
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            total += 1
            print i
    print 'total is %d'%total

find_prime()

###############################
#           No.13             #
###############################
    
'''题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。'''
def print_num():
    # all int with three digits
    for num in range(100,1000):
        hun = num / 100
        ten = num % 100 / 10
        uni = num % 10
        if hun*hun*hun + ten*ten*ten + uni*uni*uni == num:
            print num
print_num()


###############################
#           No.14             #
###############################
    
'''题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,
重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。'''



###############################
#           No.16             #
###############################
    
'''题目：输出指定格式的日期。

程序分析：使用 datetime 模块。'''

print datetime.date.today().strftime('%d/%m/%Y')
# create date obj
miyazaki_birthday = datetime.date(1941,1,5)

# use timedelta(days=1)
miyazaki_b_next = miyazaki_birthday + datetime.timedelta(days=1)
print miyazaki_b_next

# modify format
print miyazaki_b_next.strftime('%d/%m/%Y')

# replace 
first_bd = miyazaki_birthday.replace(year = miyazaki_birthday.year+1)
print first_bd.strftime('%d/%m/%Y')

###############################
#           No.17             #
###############################
    
'''题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
'''
def cal(string):
    letters, spaces, digits, others = 0, 0, 0, 0
    for i in range(len(string)):
        if string[i].isalpha():
            letters += 1
        elif string[i].isspace():
            spaces += 1
        elif string[i].isdigit():
            digits += 1  
        else:
            others += 1

    print('letters: %d, spaces: %d, digits: %d, others: %d'%(
            letters, spaces, digits, others))


cal('This is true: 3 + 5 = 8')


###############################
#           No.18             #
###############################
    
'''题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

程序分析：关键是计算出每一项的值。
'''

def na(n, a):
    mylist = []
    for i in range(1,n+1):
        mylist.append(int("{}".format(a)*i))
    return sum(mylist)

def na2(n, a):
    mysum, total = 0, 0
    for i in range(n):
        mysum += 10**i
        print('mysum: ', mysum)
        total += mysum*a        
        print('total: ', total)
    return total

print na2(4,4)        

###############################
#           No.19             #
###############################
    
'''题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。

程序分析：请参照程序Python 练习实例14。。
'''


###############################
#           No.20             #
###############################
    
'''题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

程序分析：无
'''
def cal_height(time = 10):
    # mistake made here 
    # bound_heights = 100.0
    bound_height, bound_heights = 100.0, []
    
    for i in range(2, time+1):
        bound_height /= 2 # divide by 2 for each bound
        bound_heights.append(bound_height)
    
    print bound_heights
    print('On the 10th time the ball hits the ground,'
          'it has bound height: %f'%(min(bound_heights)/2))
    
    print('On the 10th time the ball hits the ground,'
          'it has gone through %f meters in total'%(sum(bound_heights)*2+100))
        
cal_height()         

def cal_h(time=10):
    SumHeightN = 100.0
    BounceHeightN = SumHeightN/2
    for n in range(2, 11):
        SumHeightN += 2 * BounceHeightN
        BounceHeightN /= 2
    
    print 'total road is %f' % SumHeightN
    print 'the 10th bounce height is %f' % BounceHeightN

cal_h()

# mistake made here
def height():
    new_height, ori_height = 0, 100
    for i in range(1,11):
        new_height += ori_height/(2*i)
    return new_height + ori_height

height()

###############################
#           No.23             #
###############################
'''
题目：打印出如下图案（菱形）:

   *
  ***
 *****
*******
 *****
  ***
   *
   
程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，
第一层控制行，第二层控制列。

'''

from sys import stdout
for i in range(4):
    for j in range(2-i+1):
        stdout.write(' ')
    for k in range(2*i+1):
        stdout.write('*')
    print


### 
    

my_matrix  =  [[1,4,5,6,0],	[2,3,1,2,3], [8,0,9,7,1]]
def sort_matrix(amatrix, arow):
    return map(amatrix, lambda x:sorted(x[arow]))

#sort_matrix(my_matrix, 0)
my_matrix.sort(key=lambda x:x[0])
print my_matrix

lol = [range(10), range(2,12), range(5,15)]
print lol

# transpose
my_matrix = zip(*my_matrix)
my_matrix.sort(key=lambda x:x[1])
my_matrix = zip(*my_matrix)
print my_matrix

a = [
     [12, 18, 6, 3],
     [ 4,  3, 1, 2],
     [15,  8, 9, 6]
    ]
a.sort(key=lambda x:x[1])# sort by the value of 2nd column

# what we want sort 2d array by value of a row
# what we have: sort 2d array ba value of a col
# what we could do:

# transpose col -> row
# sort by col
# transpose row -> col

a = zip(*a)
a.sort(key=lambda x:x[1])
a = zip(*a)
print(a)


###############################
#           No.25             #
###############################
'''
题目：求1+2!+3!+...+20!的和。

程序分析：此程序只是把累加变成了累乘。
'''
def sum_pf_products():
    products = 1
    sums = 0
    for i in range(1,21):
        products *= i
        sums += products
    return sums
print '1! + 2! + 3! + ... + 20! = %d' % sum_pf_products()


###############################
#           No.26             #
###############################
# calculate a product recursively
'''
题目：利用递归方法求5!。
程序分析：递归公式：fn=fn_1*4!
'''
def normal(num):
    res = 1
    for i in range(1,num+1):
        res *= i
    return res

def recursive(num):
    if num == 1:
        res = 1
    else:
        res = num*recursive(num-1)
    return res
    
print recursive(5)

###############################
#           No.27             #
###############################
# print a string in reverse recursively
'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''

def output(astring, length):
    if length == 0:
        return
    print(astring[length-1])
    output(astring, length-1)


def output2(string, l):
    # stop condition
    if l == 0:
        return 
    # else
    # print the letter which is one position further than current idx
    print string[l-1]
    # call next one
    output2(string, l-1)
    
output2('Hello', len('Hello'))


###############################
#           No.28             #
###############################
'''
题目：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。
请问第五个人多大？

程序分析：利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，
需知道第四人的岁数，依次类推，推到第一人（10岁），再往回推。'''

def get_age(num):
    if num == 1 :
        res = 10
    else:
        res = get_age(num-1) + 2
    return res

get_age(5)

def fib_new(num):
    # 0、1、1、2、3、5、8、13、21、34、……
    if 0 < num < 3:
        return 1
    else:
        return fib_new(num-1) + fib_new(num-2)
print(fib_new(7))



###############################
#           No.29             #
###############################

# ??????
'''
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

程序分析：学会分解出每一位数。
'''
def units_reverse_print(num):
    # num is an int smaller than 100000
    a = num / 10000
    b = num % 10000 / 1000
    c = num % 1000 / 100
    d = num % 100 / 10
    e = num % 10
    
    if a != 0:
        print 'num has 5 digits, in reverse: ', e, d, c, b, a
    elif b != 0:
        print 'num has 4 digits, in reverse: ', e, d, c, b
    elif c != 0:
        print 'num has 3 digits, in reverse: ', e, d, c
    elif d != 0:
        print 'num has 2 digits, in reverse: ', e, d
    else:
        print 'num has 1 digits, in reverse: ', e
          

units_reverse_print(9010)








###############################
#           No.30             #
###############################
# if a num is Palindrome
'''题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

程序分析：无。
'''
def is_palindrome(the_num):
    
    for i in range(len(the_num)/2):
        # the_num here is a string
        # the first ele: num[0]
        # the last ele: num[-1]
        if the_num[i] != the_num[-i-1]:
            return False
    return True


print is_palindrome('1232321')        


###############################
#           No.31             #
###############################
'''
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。
'''
def guess():
    msg = 'Please insert a letter: '
    letter = raw_input(msg)
    if letter == 'F':
        print 'Friday'
    elif letter == 'W':
        print 'Wednesday'
    elif letter == 'M':
        print 'Monday'
    elif letter == 'T':
        letter = raw_input(msg)
        if letter == 'u':
            print 'Tuesday'
        elif letter == 'h':
            print 'Thursday'
        else:
            letter = raw_input('Invalid input, please restart: ')
            guess()
    elif letter == 'S':
        letter = raw_input(msg)
        if letter == 'a':
            print 'Saturday'
        elif letter == 'u':
            print 'Sunday'
        else:
            letter = raw_input('Invalid input, please restart: ')
    else:
        print 'Wrong input! Please insert a startting letter of a weekday in capital'
        guess()


guess()


###############################
#           No.32             #
###############################

'''
题目：按相反的顺序输出列表的值。

程序分析：无。
'''
def reverse(alist):
    return alist[::-1]

print reverse([1,2,3,4,5,6,7])


###############################
#           No.33             #
###############################

'''
题目：按逗号分隔列表。
程序分析：无。
'''
def sep_list_comma(alist):
    # return ','.join(alist) mistake made here
    return ', '.join(str(a) for a in alist) 

print sep_list_comma(['it', 'is', 'good'])

###############################
#           No.34             #
###############################

'''
题目：练习函数调用。
程序分析：无。
'''
def say_hello():
    print 'Hello World'
def say_three_times():
    for i in range(3):
       say_hello()
if __name__ == '__main__': # mistake made here __'main'__
    say_three_times()

###############################
#           No.35             #
###############################

# ???
    
'''
题目：文本颜色设置。
程序分析：无。
'''
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC

###############################
#           No.36             #
###############################
# calculate prime numbers in a certain range
'''
题目：求100之内的素数。
程序分析：无。
'''
def prime(lower, upper):
    for num in range(lower, upper+1):
        if num > 1:
            for i in range(2, num):
                if num%i == 0:
                    break
            else:
                print num

prime(1,100)

































