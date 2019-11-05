# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 22:58:20 2019
Find the index at which a given power of 2 appears in a list
@author: CHINTAN
"""
L = [1, 2, 4, 8, 16, 32, 64]
X = 5
found = False   
i = 0
while not found and i < len(L):
    if 2 ** X == L[i]:
        found = True
    else:
        i = i+1
    if found:
        print('at index', i)
    else:
        print(X, 'not found')
