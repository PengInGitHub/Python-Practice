#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""
import pandas as pd
# apply function to Series and DataFrame

add = '/Users/pengchengliu/go/src/github.com/user/Titanic/data/train.csv'
train = pd.read_csv(add)

# map() function as a Series method
# usually used for mapping cate data to num data
train['Sex_num'] = train.Sex.map({'female':0, 'male':1})
print train.Sex_num.head(3)

# compare
train.loc[0:4, ['Sex', 'Sex_num']]

# apply fun as a Series method
train['Name_length'] = train.Name.apply(len)
train.loc[0:4, ['Name_length', 'Name']]

import numpy as np
# round up float to int
train['Fare_ceil'] = train.Fare.apply(np.ceil)
train.loc[0:4, ['Fare_ceil', 'Fare']]

# apply + lambda
train.Name.str.split(',').head(4)

def get_element(mylist, position):
    return mylist[position]

train.Name.str.split(',').apply(get_element, position=0).head()

# instead, we could use lambda
train.Name.str.split(',').apply(lambda x:x[0]).head()

# getting the second string
train.Name.str.split(',').apply(lambda x:x[1]).head()

# apply fun as a DataFrame method
# apply method to travel axis = 0 (downwards, column)

train.loc[:, ['Fare', 'Age']].apply(min, axis=0)



















