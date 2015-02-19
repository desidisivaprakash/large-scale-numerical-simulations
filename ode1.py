

import numpy as np
import math
from numpy import *

#t = int(input())
#x = int(input())
x = math.pi
dx = x/4

#print dx

#For updating the boundary values
mat = np.zeros((6,5), float)
#print shape(mat)
for i in range(5):
    mat[5][i] = round((math.sin(i*dx)),2)

for t in range(6):
    mat[t][0] = 0

mat[5][0] = 0
#print mat[5][1]

#Explicit Update method
for n in range(1,6):
    for i in range(1,4):
        mat[5 - n][i] = mat[5-n+1][i] + (1/(dx**2))*(mat[5-n+1][i-1] - 2*mat[5-n+1][i] + mat[5-n+1][i+1])

print mat

'''#For updating the values of ut(scrap)
ut = np.zeros((1,4), float)

for k in range():
    for l in range():
        ut[1][] = u[] '''       
        
