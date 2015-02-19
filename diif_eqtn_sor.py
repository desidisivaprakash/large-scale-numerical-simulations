'''siva'''

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

Error = 10**(-4)
def frange(start, stop, step):
         i = start
         while i < stop:
             yield i
             i += step
def SOR(A,b):
    n = len(A)
    x_new = np.zeros(n)
    x_old = b
    weights =[]
    it=[]
    for w in frange(0,2,0.01):
        error = 10
        weights.append(w)
        iterations = 0
        x_new = np.zeros(n)
        x_old = b
        while(error>Error):
            for i in range(n):
                if A[i][i]!=0:
                    dummy = 0
                    for j in range(n):
                        if i!=j:
                            if j<i:
                                dummy = dummy + A[i][j] * x_new[j]
                            else:
                                dummy = dummy + A[i][j] * x_old[j]
                x_new[i] = (1-w) * x_old[i] + w*((b[i] - dummy)/A[i][i])
            error = max(x_new - x_old)
            x_old = copy.deepcopy(x_new)
            return x_new
            iterations = iterations + 1
        it.append(iterations)
    '''plt.plot(weights,it)
    plt.show()'''


A1 = make_matA(10)
A2 = make_matB(10)
#print SOR(A1,A2)
print np.shape(A2)
print np.shape(A1)
