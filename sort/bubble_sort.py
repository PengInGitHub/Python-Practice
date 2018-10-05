#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""

def bubble_sort(seq):
    if len(seq) < 2:
        return seq
    
    # outter loop, iterate each num in seq
    for i in range(len(seq)-1):
        # inner loop, iterate each num in seq behind i
        for j in range(len(seq)-i-1):
            # swap if previous num is larger than the one after it
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq

def bubble_sort_new(seq):
    if len(seq) < 2:
        return seq
    # outter loop, from len(seq)-1, ..., 3, 2, 1
    start, stop, step = len(seq)-1, 0, -1
    for i in range(start, stop, step):
        # inner loop, from 0,1, ... i
        for j in range(i):
            if seq[j] > seq[j+1]:
                # swap
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq

res = bubble_sort_new([3,-3,50,-50,50,50,2])
bench = sorted([3,-3,50,-50,50,50,2])
res2 = bubble_sort_new([3])
print(res)









