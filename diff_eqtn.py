

import numpy as np
import math
import copy
#Global Variables
Error = 10**(-4)

def make_matA(N):
    A = np.zeros((N-1,N-1),float)
    for i in range(N-1):
        for j in range(N-1):
            if i==j and i>=0 and j>0:
                A[0][0] = -2.002
                A[i][j] = -2.002
                A[i][j-1] = 1
                A[i-1][j] = 1

    return A

def make_matB(N):
    B = np.zeros((N-1,1),float)
    B[0][0] = -300.4
    B[N-2][0] = -400.4
    for k in range (1,N-2):
        B[k][0] = -0.4
    return B


Error = 10**(-10)

def guass_siedel(A,b):
    n = len(A)
    x_new = np.zeros(n)
    x_old = np.zeros(n)
    error =20
    while(error>Error):
    #for _ in range(2200):
        for i in range(n):
            if A[i][i]!=0:
                dummy = 0
                for j in range(n):
                    if i!=j:
                        if j<i:
                            dummy = dummy + A[i][j] * x_new[j]
                        else:
                            dummy = dummy + A[i][j] * x_old[j]
            x_new[i] = (b[i] - dummy)/A[i][i]
            error = max(x_new - x_old)
            x_old = copy.deepcopy(x_new)
    return x_new






A1 = make_matA(10)
A2 = make_matB(10)
print guass_siedel(A1,A2)



