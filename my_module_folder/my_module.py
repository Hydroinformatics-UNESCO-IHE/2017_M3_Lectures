# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 16:56:28 2017

@author: chaco3
"""

c = 10

def print_a():
    print('this is the letter a')
    return

def print_args(*add_args):
    print('These are the arguments {0}'.format(add_args))
    return

def print_module_constant():
    print(c)
    return