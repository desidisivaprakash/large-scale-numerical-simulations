# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 14:50:42 2014

siva
"""
import matplotlib.pyplot as plt 
#a=[[4,-1,0,0,0],[-1,4,-1,0,0],[0,-1,4,-1,0],[0,0,-1,4,-1],[0,0,0,-1,4]]
#b=[2,1,1,1,2]
#x=[1]*len(a)
def jacobirossor(a,b,x,detX,n):
    y=0
    w=1.2
    h=[]
    for i in range(n):
        h.append(i*detX)
    for iteraion in range(0,10000):
        y=[0]*len(x)
        for j in range(0,len(a)):    
            arr=0
            for i in range(0,len(b)):
                if j!=i:
                    arr=arr+(a[j][i]*x[i])
            y[j]=w*(b[j]-arr)*1.0/a[j][j]+(1-w)*x[j]
            x[j]=y[j]
        z=[]        
        for count in range(0,len(a)):    
            arr1=0
            for count1 in range(0,len(b)):
                arr1=arr1+(a[count][count1]*x[count1])
            z.append(arr1-b[count])
        norm=0
        norm1=0
        for i in range(0,len(z)):
            norm=norm+z[i]*z[i]
            norm1=norm1+x[i]*x[i]
        import math
        norm=math.sqrt(norm)
        norm1=math.sqrt(norm1)
        print norm/norm1
        if norm/norm1<0.001:
            print 'answer',norm/norm1
            print iteraion
            break
    plt.plot(h,x)           
    return x
#print jacobirossor(a,b,x)
