# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:56:46 2019
Use of for else
@author: CHINTAN
"""
L=[2**i for i in range(6)]
X = 10 
for i in range(len(L)):
    if L[i]!=2**X:
        print(X,'not found')
    else:
        print('at index',i)
        break
