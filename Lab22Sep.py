# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 15:04:28 2014

@author: siva
"""
import time
time_code=time.time()
interval=10
h=1.0/interval
arr=[]
for i in range(0,interval+1):
    arr.append([0]*(interval+1))
for count in range(0,interval+1):
    import math    
    arr[0][count]=(h*count-1)*math.sin(count*h)
    arr[count][0]=0
    arr[interval][count]=count*h*(2-(count*h))
    arr[count][interval]=count*h
for iteration in range(0,100000):
    for k in range(1,len(arr)-1):
        for l in range(1,len(arr)-1):
            arr[k][l]=0.25*(arr[k-1][l]+arr[k][l-1]+arr[k+1][l]+arr[k][l+1])
print
for i in range(0,len(arr)):
    print arr[i]
time_code=time.time()-time_code
print '\n', time_code
