# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 13:54:16 2014

@author: siva
"""


def create(deltax):
    n=int(10/deltax)
    a=[[0]*(n-1)]
    for i in range(2,n):
        a=a+[[0]*(n-1)]
    b=[0]*(n-1)
    h=0.05
    
    y0=300
    b[0]=h*200*deltax*deltax+y0
    yn=400
    b[n-2]=h*200*deltax*deltax+yn
    a[0][0]=2+h*deltax*deltax
    a[0][1]=-1
    a[n-2][n-2]=2+h*deltax*deltax
    a[n-2][n-3]=-1
    for i in range(1,n-2):
        a[i][i-1]=-1
        a[i][i]=2+h*deltax*deltax
        a[i][i+1]=-1
        b[i]=h*200*deltax*deltax
    return a,b

subinter=int(raw_input('give subinterval values'))
deltax=10.0/int(subinter)
var=create(deltax)
n=subinter
xaxis=[0]

count=0

for i in range(0,n):
    count=count+deltax
    xaxis.append(count)
import sor
x=[200]*(n-1)
s=sor.jacobirossor(var[0],var[1],x)
s.append(400)
s.insert(0,300)
import matplotlib as pyt
print len(s),len(xaxis)
pyt.pyplot.plot(xaxis,s)
pyt.pyplot.show()
