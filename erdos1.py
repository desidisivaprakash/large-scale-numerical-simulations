#D SIVA PRAKASH
#UG201113010

import random
import numpy
import networkx as nx
import matplotlib.pyplot as plt

n= int(raw_input())
e=int(raw_input())


def erdos(n,e):
    G=nx.Graph()
    m= numpy.zeros([n,n],int)
    c=n*(n-1)/2
    if e>c:
        e=c
    for i in range(n):
        G.add_node(i)
    for k in range(e):
        a=random.randrange(n)
        b=random.randrange(n)
        if a==b or m[a][b]==1 or m[b][a]==1:
            k=k-1
        else:
            m[a][b]=1
            m[b][a]=1

    for i in range(n):
        for j in range(n):
            if m[i][j]==1:
                G.add_edge(i,j)
    pos = nx.shell_layout(G)
    nx.draw(G,pos)
    plt.show()
    return m

print erdos(n,e)


