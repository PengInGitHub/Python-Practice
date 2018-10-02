#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""

import curses
from collections import defaultdict
from random import randrange, choice

# usage of random.randrange, random.choice
# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list

# build dict of user input - program action
letter_codes = ['W', 'A', 'S', 'D', 'R', 'Q', 'w', 'a', 's', 'd', 'r', 'q']
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
action_dict = dict(zip(letter_codes, actions*2))


def invert():
    

class GameField():
    def __ini__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0
        self.high_score = 0
        self.reset()
    
    def move(self, direction):
        def move_row_left(row):
            # step 1: remove all 0 on the left side, add 0 to the tail
            def tighten(row):
                # remove all 0
                new_row = [i for i in row if i != 0 ]
                # add 0 to the tail of new_row
                new_row += [0 for i in range(len(row) - len(new_row))]
                # return the tightened row
                return new_row
            
            # step 2: merge same numbers
            def merge(row):
                pair = False
                new_row = []
                # iterate elements in row
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += 2 * row[i]
                        pair = False
                    
                    # if not identical
                    else:
                        # if two neighbor nums are identical
                        if i + 1 < len(row) and row[i] == row[i+1]:
                            pair = True
                            new_row.append(0)
                        # if not identical
                        else:
                            new_row.append(row[i])
                
                # If the expression is false, Python raises an
                # AssertionError exception
                assert len(new_row) == len(row)
                return new_row
            return tighten(merge(tighten(row)))
        
        # init a dict
        moves = {}
        moves['Left'] = lambda field: [move_row_left(row) for row in field]
        moves['Right'] = lambda field: invert(moves['Left'](invert(field)))
        


























        