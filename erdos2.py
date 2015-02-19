#D SIVA PRAKASH
#UG201113010

import random
import numpy

n= int(raw_input())
e=int(raw_input())
const=int(raw_input())

def erdos(n,e):
    m= numpy.zeros([n,n],int)
    c=n*(n-1)/2
    totalsum=0
    d=e/c
    for f in range(const):
        for k in range(e):
            x=(random.randrange(10))/10
            a=random.randrange(n)
            b=random.randrange(n)
            if a!=b and m[a][b]!=1 and m[b][a]!=1 and d>=x:
                m[a][b]=1
                m[b][a]=1
        k=0
        for i in range(n):
            for j in range(n):
               k=k+m[i][j]
        totalsum=totalsum+k
    totalsum = totalsum/const
    print totalsum/2



print erdos(n,e)



