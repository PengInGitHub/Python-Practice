#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""
# resource
# http://www.cnblogs.com/xuyaping/p/6705848.html

import math


##################
#      map       #
##################

# deal with list
name = ['alex', 'yunhan', 'ahmed']
name_sufix = map(lambda i:i+"_sb" ,name)
name_sufix2 = [(n+"_sb").capitalize() for n in name]
name_capital = map(lambda i:i.capitalize() ,name)
capital = [n.capitalize() for n in name]
print name_capital

# deal with list of dict
l = [{'name':'Alex'}, {'name':'Yunan'}]
l_name = map(lambda k:k['name'], l)
print l_name


#####################
#      filter       #
#####################
shares = {
        'IBM':36.6,
        'Google':260.4,
        'Alibaba': 160.2,
        'Tencent': 56.2
        }

def filter_complex(shares):
    res = []
    for share in shares:
        if shares[share] > 150:
            res.append(share)
    return res

filter_light = filter(lambda key:shares[key]>150, shares)
print list(filter_light)

#####################
#      reduce       #
#####################

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

total_value = map(lambda i:math.floor(i['shares']*i['price']) , portfolio)
print reduce(lambda x,y:x+y, list(total_value))
print sum(total_value)

print filter(lambda x:x['price']>100, portfolio)
















