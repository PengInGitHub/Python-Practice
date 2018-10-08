#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""
# list comprehensions provides a concise way to create lists

# [i*i for i in some_list if i in another_list]

# before
'''new_list = []
for i in old_list:
    if filter(i):
        new_list.append(expressions(i))
        
# after
new_list = [expressions(i) for i in old_list if filter(i)]

# same as

for item in list:
    if conditional:
        expression
'''
print [i for i in range(11) if i % 2 == 0][1:]
print range(11)[::-1]


# get squares of int btw 0 and 10
squares = []
for i in range(10):
    squares.append(i*i)


new = [i*i for i in range(10)]
print new
print [i*3 for i in range(10)]

print [i.lower() for i in ['ABC', 'DF', 'FG']]

a = 'Hello this is ID.89757'
print [i for i in a if i.isdigit()]
print [i for i in a if i.isalpha()]

fh = open("test.txt", "r")
res = [i for i in fh if "line3" in i]
print res

print [x+y for x in [50,60,20] for y in [2,3,59]]



















