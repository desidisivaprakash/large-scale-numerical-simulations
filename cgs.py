# -*- coding: utf-8 -*-
"""
Created on Wed Oct 01 11:15:37 2014

@author: siva
"""

import scipy.sparse.linalg as sp
import numpy as np
tn=200
t10=400
delX=0.1
to=300
beta=-.05*tn*(delX**2)
alpha=-(2+(.05)*(delX**2))
n=100


a=np.zeros((n,n),dtype=float)
for i in range(n):
    for j in range(n):
        if i==j:
            a[i,i]=alpha
        elif(i==j+1 or i==j-1):
            a[i,j]=1
            
#print a            
b=[]
for i in range(n):
    if ( i==0  ) :
        b.append(beta-to)
    elif(i==n-1):
        b.append(beta-t10)
    else :
        b.append(beta)            

#print b    
x=[1]*len(a)

result=sp.cgs(a, b, tol=1.e-05)
print result
