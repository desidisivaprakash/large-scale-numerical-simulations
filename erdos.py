#D SIVA PRAKASH
#UG201113010

import random
import numpy

def graph(n,e):
    m = numpy.zeros([n,n], int)
    k = 0
    while(k<e):
        i = random.randrange(0, n)
        j = random.randrange(0, n)
        if i!=j and m[i][j] == 0:
            m[i][j] = 1
            m[j][i] = 1
            k += 1

    return m

print graph(10,20)

