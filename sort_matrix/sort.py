#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""
###############################
#          sort matrix        #
###############################
    

my_matrix  =  [[1,4,5,6,0],	[2,3,1,2,3], [8,0,9,7,1]]

# this one is wrong
def sort_matrix(amatrix, arow):
    return map(lambda x:sorted(x[arow]), amatrix)

print sort_matrix(my_matrix, 1)

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
a.sort(key=lambda x:x[1])
print a 
# sort by the value of 2nd column

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
# sort a matrix by row
def sort_matrix1(a,row):
    # transpose
    a = zip(*a)
    # sort by col
    # map(a, lambda a: sorted(a[row]))
    a.sort(key = lambda x:x[row])
    # transpose
    a = zip(*a)
    return a
    
    

a = [
     [12, 18, 6, 3],
     [ 4,  3, 1, 2],
     [15,  8, 9, 6]
    ]
#a_new = map(lambda x:sorted(x[1]), a)
print a_new

print sort_matrix1(a,1)

f00 = lambda x:x/2
print f00(10)

#map([10,12,14], lambda x:x/2)
a = [10,12,14]
a_new =  map(lambda x:x/2, a)
print a_new

a.apply(lambda x:x/2)