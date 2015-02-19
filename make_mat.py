'''siva'''


import numpy as np
import math
#import matplotlib.pyplot as plt

#Global Variables
Error = 10**(-4)

def make_matA(N):
    A = np.zeros((N-1,N-1),float)
    for i in range(N-1):
        for j in range(N-1):
            if i==j:
                A[i][j] = -2.002
                A[i][j-1] = 1
                A[i-1][j] = 1
                
    return A

def make_matB(N):
    B = np.zeros((N-1,1),float)
    B[0][0] = -299.996
    B[N-2][0] = -399.96
    for k in range (1,N-2):
        B[k][0] = 0.04
    return B
        
def jacobirossor(a,b,x):
    y=0
    w=1.202127302
    itermatrix=[]

    for iteraion in range(0,2200):
        y=[0]*len(x)
        for j in range(0,len(a)):
            arr=0
            for i in range(0,len(b)):
                if j!=i:
                    arr=arr+(a[j][i]*x[i])
            y[j]=w*(b[j]-arr)*1.0/a[j][j]+(1-w)*x[j]
            x[j]=y[j]

    print type(iteraion), iteraion
    itermatrix.append(iteraion)
    #break
    h=[c for c in range(len(itermatrix))]
    #plt.plot(h,itermatrix,'ro')
    #plt.autoscale(enable=True, axis='both')
    print 'len h=', len(h),type(itermatrix), 'len iter=', (itermatrix)
    return x




A1 = make_matA(10)
A2 = make_matB(10)
x = [1]*len(A1)
print jacobirossor(A1,A2,x )



#print make_matB(10)
    
    
