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
actions_dict = dict(zip(letter_codes, actions*2))


def invert(field):
    # use extended slice
    # https://docs.python.org/release/2.3.5/whatsnew/section-slices.html
    # negative value work to make a copy of the same list in reverse order
    return [row[::-1] for row in field]
    
def transpose(field):
    # use zip(*a_matrix)
    # https://stackoverflow.com/questions/17037566/transpose-a-matrix-in-python
    return [list(row) for row in zip(*field)]
    # return map(list, zip(*field))
    # return numpy(field.transpose())

class GameField():
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0
        self.highscore = 0
        self.reset()
 
    def get_user_action(self, keyboard):
        char = "N"
        while char not in actions_dict:
            char = keyboard.getkey()
        return actions_dict(char)
 
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()
        
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
        
        # init a dict to store action-programm function pair
        moves = {}
        moves['Left'] = lambda field: [move_row_left(row) for row in field]
        moves['Right'] = lambda field: invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field : transpose(moves['Left'](transpose(field)))
        moves['Down'] =lambda field: transpose(moves['Right'](transpose(field))) 
        
        # response to action
        if direction in moves:
            if self.move_is_possible(direction):
                # modify field
                self.field = moves[direction](self.field)
                # generate new numbers
                self.spawn()
                return True
            else:
                return False
    
    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)
 
    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)
  
    def draw(self, screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '    (R)Restart (Q)Exit'
        gameover_string = '      GAME OVER'
        win_string = '        YOU WIN'
        
        def cast(string):
            screen.addstr(string + '\n')
            
        def draw_hor_separator():
            line = '+' + ('+------' * self.width + '+')[1:]
            separator = defaultdict(lambda: line)
            if not hasattr(draw_hor_separator, "counter"):
                draw_hor_separator.counter = 0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1   
        
        def draw_row(row):
            cast(''.join('|{: ^5}'.format(num) if num > 0 else '|   ' for num in row) + '|')
    
        screen.clear()
        cast('SCORE: ' + str(self.score))
        if 0 != self.highscore:
            cast('HIGHSCORE: ' + str(self.highscore))
            
        for row in self.field:
            draw_hor_separator()
            draw_row(row)
        draw_hor_separator()
        
        if self.is_win():
            cast(win_string)
        else:
            if self.is_gameover():
                cast(gameover_string)
            else:
                cast(help_string1)
        cast(help_string2)
        
    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        # TODO what is random.choice()
        (i, j) = choice([(i, j ) for i in range(self.width) 
            for j in range(self.height) if self.field[i,j] == 0])
        # input new ele to field
        self.field[i,j] = new_element
        
    def move_is_possible(self, direction):
        # test if a row could move to left
        def row_is_left_movable(row):
            # to i th ele in the row, if the ele is either zero or 
            # equal to the ele next to it (row[i]==row[i+1])
            def change(i):
                if row[i] == 0 and row[i+1] != 0:
                    return True
                if row[i] != 0 and row[i+1] == row[i]:
                    return True
                return False
            return any(change(i) for i in range(len(row)-1))
        
        # init a dict to store direction-if movable pair
        check = {}
        check['Left'] = lambda field: \
            any (row_is_left_movable(row) for row in field)
        check['Right'] = lambda field: \
            check['Left'](invert(field))
        check['Up'] = lambda field: \
            check['Left'](transpose(field))
        check['Down'] = lambda field: \
            check['Right'](transpose(field))
            
        # do the check
        if direction in check:
            return check[direction](self.field)
        else:
            return False
    
    # main login of the game
    # iterate from 5 conditions: init, game, win, loss, not_game
    def main(stdscr):
        def init():
            game_field.reset()
            return 'Game'
        
        def not_game(state):
            # draw the interface of game over or win
            game_field.draw(stdscr)
            # judge if restart or exit according to player's action
            action = game_field.get_user_action(stdscr)
            # dict of responses
            responses = defaultdict(lambda: state)
            responses['Restart'], responses['Exit'] = 'Init', 'Exit'
            return responses[action]
        
        def game():
            # draw the current status of play field
            game_field.draw(stdscr)
            # get user action
            action = game_field.get_user_action(stdscr)
            
            if action == 'Restart':
                return 'Init'
            if action == 'Exit':
                return 'Exit'
            # make a move successfully
            if game_field.move(action):
                if game_field.is_win():
                    return 'Win'
                if game_field.is_gameover():
                    return 'Gameover'
            return 'Game'
        
        state_actions = {
                'Init': init,
                'Win': lambda: not_game('Win'),
                'Gameover': lambda: not_game('Gameover'),
                'Game': game                
                }

        curses.use_default_colors()
        
        game_field = GameField(win=32)
        
        state = 'Init'
        # start to iterate
        while state != 'Exit':
            state = state_actions[state]()
        
    curses.wrapper(main)






















        