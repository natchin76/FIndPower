# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:51:24 2019
for loop removed:L created using list comprehension
@author: CHINTAN
"""

L=[2**i for i in range(6)]
X = 10
i=0
while i < len(L) and L[i]!=2**X:
    print(X,'not found')
    i=i+1
else:
    print('at index',i)    
    
