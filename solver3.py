'''##siva##'''

import sys
import copy
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
import math

from numpy import matrix







def drange(start, stop, step):
	r = start
	while r < stop:
		yield r
		r += step




def initial_guess(a):
	#i = 0
	#sample = []

	#for rows in a:
		#i += 1	
		#sample.append(i)
	
	#random.shuffle(sample)
	
	#print sample
	sample= [0 for x in xrange(len(a))]
	return sample



	
	

def condition_check(x, y):
	##Change value of tolerence in here:
	epsilon = 0.0001
	
	for i in xrange(len(x)):
		if (abs(x[i] - y[i])) <= epsilon:
			continue
		else:
			#print "True"
			return True
			
	#print "False"
	return False





def gauss_seidel(a, b):
	X = initial_guess(a)
	condition = True
	
	count2 = 0
	while condition == True:
		
		prev_X = copy.deepcopy(X)
		for i in xrange(len(X)):
		
			sum = 0
			for j in xrange(len(X)):
				
				if j != i:
					sum += (a[i][j])*(X[j])
							
			X[i] = (1.0/a[i][i])*(b[i] - sum)
		
		condition = condition_check(prev_X, X)

		count2 += 1
		print count2
	print "Total iterations for solving equations by Gauss-Seidel method:", count2
	
	'''points = []
	for as_point in xrange(Nx):
		points.append(as_point*0.01)
	
	plt.plot(points, X)
	plt.xlabel('Length')
	plt.ylabel('Temperature')
	plt.title('Temperature variation alog the length of the rod')
	plt.grid(True)
	plt.savefig("output_rod_200_rand.png")
	plt.show()'''
	
	return X








def main():
	#Solving 2D PDEs
	#x and y belongs in [0,1]
	
	print "Number of points along X-axis and Y-axis: "
	n_dim = eval(raw_input())

	unknowns = (n_dim + 1)**2 - 4*n_dim
	
	#Initializing A matrix
	A = [[0 for x in xrange(unknowns)] for x in xrange(unknowns)]

	#Variable are r[1,1] through r[9,9]
	knowns = [[0 for x in xrange(n_dim + 1)] for x in xrange(n_dim + 1)]
	
	for i in xrange(n_dim):
		knowns[0][i] = 0
		knowns[n_dim][i] = 0.1*i
		knowns[i][0] = (0.1*i - 1)*math.sin(0.1*i)
		knowns[i][n_dim] = (0.1*i)*(2 - 0.1*i)
	
	#print knowns	
	sub_matrix_dim = unknowns/(n_dim - 1)
	
	for i in xrange(unknowns):
		for j in xrange(unknowns):
		
			if i == j:
				A[i][j] = 4
			
			elif (j == i+1 and j%sub_matrix_dim != 0) or (j == i-1) or j == i+sub_matrix_dim or j == i-sub_matrix_dim:
				A[i][j] = -1			
	
	
	B = [0 for i in xrange(unknowns)]
	
	j = 0
	k = 0
	l = 0
	m = 0
	for i in xrange(unknowns):
		if (i%sub_matrix_dim != 0) and (i%sub_matrix_dim != sub_matrix_dim - 1):
			B[i] = 0  
		elif i%sub_matrix_dim == 0:
			B[i] = knowns[0][j]
			j += 1
		elif i%sub_matrix_dim == sub_matrix_dim - 1:
			B[i] = knowns[n_dim][k]
			k += 1		
		
		if i in xrange(0, sub_matrix_dim):
			B[i] = B[i] + knowns[l][0]
			l += 1
			
		if i in xrange(unknowns - sub_matrix_dim, unknowns):		
			B[i] = B[i] + knowns[m][n_dim]
			m += 1
	
	for element in B:
		print element
				
	solution = gauss_seidel(A, B)
	print "Solution:"
	
	for i in xrange(unknowns):
		print solution[i]
		if i % sub_matrix_dim == 0:
			print "\n"
	return 2





if __name__ == "__main__":
	sys.exit(main())
