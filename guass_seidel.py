'''siva'''

import numpy as np

Error = 10**(-6)

def guass_siedel(A,b):
    n = len(A)
    x_new = np.zeros(n)
    x_old = np.zeros(n)
    error =20
    count=0
    while(error>Error):
        count=count+1
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
        x_old = x_new
        print x_new
    print "iterations: ",count
    return x_new
    
def inputs():
    n = input('size of array?')
    B = [[0]*n for i in range(n)]
    const = [[0]*n]
    B = input('Matrix in list form')
    const = input('Values of b in list form')
    A = np.asarray(B)
    b = np.asarray(const)
    print guass_siedel(A,b)

inputs()
