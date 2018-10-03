#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""

def max_complex(x, y):
    return (x > y) * x + (x < y) * y + (x==y)*x

def min_complex(x, y):
    return (x > y) * y + (x < y) * x + (x==y)*x

max_simple = lambda x,y : (x>y)*x + (x<=y)*y
min_simple = lambda x,y : (x>y)*y + (x<=y)*x

print ' The larger value is: %d\n' % max_simple(20,10)
print ' The smaller value is: %d' % min_simple(10,20)