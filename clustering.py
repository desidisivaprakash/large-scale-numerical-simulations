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
    f=numpy.zeros(n,int)
    cluster=numpy.zeros(n,float)
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
        demo = v[i] * (v[i]-1)
        nemo=0

        for j in range(n):
            s=0
            for k in range(n):
                s = s+(m[i][j] * m[i][k] * m[k][j])
            nemo=nemo+s
        if demo>0:
            cluster[i] = float(nemo)/ float(demo)


    for i in range(n):
        f[i]=i

    pl.hist(cluster,range = (cluster.min(),cluster.max()))
    pl.xlabel("Clustering Quotient")
    pl.ylabel("Frequency")
    pl.show()
    print cluster
erdos(n,e)


