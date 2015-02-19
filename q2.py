

import numpy as np
import math
from numpy import *


x = math.pi
t = 10

#k--->N_x
k=10
dt=t/k
#l--->N_t
l=4
dx=x/l
#print dx

#For updating the boundary values
mat = np.zeros((k+1,l+1), float)
#print shape(mat)
for i in range(l+1):
    mat[k][i] = round((math.sin(2*(i*dx))),2)

for t in range(k+1):
    mat[t][0] = 0

mat[k][0] = 0


#Explicit Update method
for n in range(1,k+1):
    for i in range(1,l):
        mat[k - n][i] = mat[k-n+1][i] + ((dt/(dx**2)))*(mat[k-n+1][i-1] - 2*mat[k-n+1][i] + mat[k-n+1][i+1])


print mat

      
        
