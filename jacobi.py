'''siva'''

import numpy as np

Error = 10**(-6)

def diagonal_mat(A):
    n = len(A)
    D = np.zeros((n,n),int)
    for i in range(n):
        for j in range(n):
            if i == j:
                D[i][j] = A[i][j]            
    R = A-D
    return (D,R)


def jacobi(A,b):
    n = len(A)
    D,R = diagonal_mat(A)
    x_new = np.zeros(n,int)
    x_old = np.zeros(n,int)
    invD = np.linalg.inv(D)
    error = 20
    count=0
    while(error>Error):
        count = count+1
        R_new = np.dot(R,x_old)
        b_new = b - R_new
        x_new = np.dot(invD,b_new)
        error = max(x_new - x_old)
        x_old = x_new
        #print x_new
    #print "iterations: ",count
    return x_new
    
    
def inputs():
    n = input('size of array?')
    B = [[0]*n for i in range(n)]
    const = [[0]*n]
    B = input('Matrix in list form')
    const = input('Values of b in list form')
    A = np.asarray(B)
    b = np.asarray(const)
    print jacobi(A,b)

inputs()    
