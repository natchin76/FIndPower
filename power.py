"""
Created on Wed Nov  6 16:51:24 2019
USe of while else statement
@author: CHINTAN
"""

L=[2**i for i in range(6)]
X = 3 
i = 0
while i < len(L) and 2**X!=L[i]:
    print(X,'not found')
    i=i+1
else:
    print('at index',i)    
