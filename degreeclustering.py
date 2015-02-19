#D SIVA PRAKASH
#UG201113010


import random
import numpy
import matplotlib.pyplot as pl

n= int(raw_input())
e=int(raw_input())

def erdos(n,e):
    m= numpy.zeros([n,n],int)
    v= numpy.zeros(n,int)
    dummy= numpy.zeros(n,int)
    f=numpy.zeros(n,int)
    c=n*(n-1)/2
    totalsum=0
    d=e/c


    for k in range(c):
        x=(random.randrange(9))/10
        a=random.randrange(n)
        b=random.randrange(n)
        if a!=b and m[a][b]!=1 and m[b][a]!=1 and d>=x:
            m[a][b]=1
            m[b][a]=1
    k=0
    for i in range(n):
        k=0
        for j in range(n):
            k=k+m[i][j]
        v[i]=k

    for i in range(n):
        f[v[i]]=f[v[i]]+1

    for i in range(n):
        dummy[i]=i
    fh=open("degree.txt","w")

    for i in range(0,n):
        fh.write(str(v[i])+"\n")
    fh.close()

    #pl.plot(dummy,f)
    #pl.show()

erdos(n,e)


