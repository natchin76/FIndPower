"""
Created on Tue Nov  5 22:58:20 2019
Find the index at which a given power of 2 appears in a list
Used for loop to create List L
@author: CHINTAN
"""
L=[2**i for i in range(6)]
X = 5
i = 0
while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    else:
        i = i+1
        print(X, 'not found')
