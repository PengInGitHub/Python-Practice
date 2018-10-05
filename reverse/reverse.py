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















