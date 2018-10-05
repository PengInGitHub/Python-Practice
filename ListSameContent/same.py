#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""

# compare if two lists have identical contents, order irrelevant

def equal_content(list1, list2):
    return len(list1) == len(list2) and sorted(list1)==sorted(list2)

if __name__ == "__main__":
    l1, l2 = [2,3,4,5,6], [3,2,6,5,4]
    l3, l4 = [2,3,4,5,6], [-3,2,6,5,4]    
    print equal_content(l3, l4)