# -*- coding: utf-8 -*-
"""
Created on Wed Oct 01 10:19:59 2014

@author: siva
"""

from numpy import dot
from math import sqrt
 
def conjGrad(Av,x,b,tol=1.0e-9):
    n = len(b)
    r = b - Av(x)
    s = r.copy()
    for i in range(n):
        u = Av(s)
        alpha = dot(s,r)/dot(s,u)
        x = x + alpha*s
        r = b - Av(x)
        if(sqrt(dot(r,r))) < tol:
            break
        else:
            beta = -dot(r,u)/dot(s,u)
            s = r + beta*s
    return x,i
    
Av=[]
b=[]
x=[]
print conjGrad(Av,x,b,tol=1.0e-9)    
