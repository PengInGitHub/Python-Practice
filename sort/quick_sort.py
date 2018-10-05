#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""

def qsort(a_list):
    if a_list == []:
        return []
    pivot = a_list[0]
    less = qsort([i for i in a_list[1:] if i < pivot])
    more = qsort([i for i in a_list[1:] if i >= pivot])
    return less + [pivot] + more

def qsort_ori(seq):
    if len(seq) < 2:
        return seq
    
    pivot = seq[0]
    less, equal, more = [], [], []
    
    for x in seq:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            more.append(x)
    return qsort_ori(less) + equal + qsort_ori(more)


res = qsort_ori([3,-3,50,-50,50,50,2])
res2 = qsort_ori([3])
print(res)