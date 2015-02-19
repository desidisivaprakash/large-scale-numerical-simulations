# -*- coding: utf-8 -*-
"""
Created on Wed Oct 01 00:07:44 2014

@author: siva
"""
import numpy as np
from scipy.linalg import solve

def jacobi(A, b, x, n):

    D = np.diag(A)
    R = A - np.diagflat(D)
    
    for i in range(n):
        x = (b - np.dot(R,x))/ D
        print str(i).zfill(3),
        print(x)
    return x

'''___Main___'''

A = np.array([[5,-2,3],[-3,9,1],[2,-1,7]])
b = [-1.0, 2.0, 3.0]
x = [0, 0, 0]
n = 7

print("\n\ninit"),
print(x)
print("")
x = jacobi(A, b, x, n)
print("\nSol "),
print(x)
print("Act "),
print solve(A, b)
print("\n")
