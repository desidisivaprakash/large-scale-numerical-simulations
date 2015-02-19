

import numpy as np
beta=-.4
alpha=-2.002
n=10
to=300
tn=400
a=np.zeros((n,n),dtype=float)
for i in range(n):
    for j in range(n):
        if i==j:
            a[i,i]=alpha
        elif(i==j+1 or i==j-1):
            a[i,j]=1

print a
b=[]
for i in range(n):
    if ( i==0  ) :
        b.append(beta-to)
    elif(i==n-1):
        b.append(beta-tn)
    else :
        b.append(beta)

print b
