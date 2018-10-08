#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""
# resource
# https://blog.csdn.net/Jerry_1126/article/details/44023949

# reverse a string
my_string = 'abcdefg'
my_reverse = my_string[::-1]
my_list = [1,2,3,4,5,6]
print my_list[::-1]

# constuct dict from two paired lists 
l1 = ['US', 'China', 'Japan', 'Germany']
l2 = [1, 2, 3, 4]
gdp_rank = dict(zip(l1,l2))
print gdp_rank

# concat strings
strings = ['US', 'China', 'Germany']
print ' '.join(strings)



# merge sort
# divide - divide a list into several parts
# merge - merge sorted lists, compare the first ele and modify the idx
def merge_sort(alist):
    if len(alist) < 2:
        return alist
    mid = len(alist)/2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    return merge(left, right)

def merge(left, right):
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res
        
      
  
# bubble sort
def bubble_sort(alist):
    if len(alist) < 2:
        return alist
    start, stop, step = len(alist)-1, 0, -1
    # outter loop 
    for i in range(start,stop,step):
        # inner loop
        for j in range(i):
            # if front one larger than behind one
            if alist[j] > alist[j+1]:
                # swap
                alist[j], alist[j+1] = alist[j+1], alist[j]
                
    return alist

alist = [54,26,93,17,77,31,44,55,20,20,0,-20]


# merge sort
# divide: seperate the lists into single pieces
# merge: merge sorted lists, compare with the first values, modify idx

def merge_sorts(alist):
    if len(alist) < 2:
        return alist
    mid = len(alist)/2
    left = merge_sorts(alist[:mid])
    right = merge_sorts(alist[mid:])
    return merged(left, right)

def merged(left, right):
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
           res.append(left[i])
           i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res


# bubble sort
def bubble(alist):
    if len(alist) < 2:
        return alist
    
    # outter loop    
    start, stop, step = len(alist)-1, 0, -1
    for i in range(start, stop, step):
        # inner loop
        for j in range(i):
            # compare
            if alist[j] > alist[j+1]:
                # swap
                alist[j], alist[j+1] = alist[j+1], alist[j]
                
    return alist



# quick sort
# use pivot, binary dividing
def quick(alist):
    if len(alist) < 2:
        return alist
    pivot = alist[0]
    smaller, equal, larger = [], [], []
    for num in alist:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)
    return quick(smaller) + equal + quick(larger)


'''print(mergedd) '''


# complete the code
import os

def print_directory_contents(sPath):
    """
    这个函数接受文件夹的名称作为输入参数，
    返回该文件夹中文件的路径，
    以及其包含文件夹中文件的路径。

    """
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            # recursion
            print_directory_contents(sChildPath)
        else:
            print sChildPath
    # 补充代码

'''
print_directory_contents("/Users/pengchengliu/Documents/GitHub/Python_Practice/BunniesAndBadgers")
'''

# list comprehension

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# A0: {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

A1 = range(10)
# A1: 0, 1, 2, ... 9

A2 = [i for i in A1 if i in A0]
# A2: []

A3 = [A0[s] for s in A0]
# 1, 2, 3, 4, 5

A4 = [i for i in A1 if i in A3]
# [1, 2, 3, 4, 5]

A5 = {i:i*i for i in A1}

A6 = [[i,i*i] for i in A1]
print A6

### what the output would be

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print l

f(2)
# 0, 1
f(3,[3,2,1])
# 3, 2, 1, 0, 1, 4
f(3)
# 0, 1, 4 --- wrong!
# 0, 1, 0, 1, 4
# this is b/c f(3) used the same list of f(2), so the res of f(2) is in f(3)











