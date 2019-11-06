# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 22:58:20 2019
Find the index at which a given power of 2 appears in a list(found flag removed)
@author: CHINTAN
"""
L = [1, 2, 4, 8, 16, 32, 64]
X = 3
i = 0
while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    else:
        i = i+1
        print(X, 'not found')
