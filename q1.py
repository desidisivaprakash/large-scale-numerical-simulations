

import sys
import copy
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

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
	
	points = []
	for as_point in xrange(Nx):
		points.append(as_point*delta_x - 1)
	
	plt.plot(points, X)
	plt.xlabel('Length (x)')
	plt.ylabel('y')
	plt.title('Variation of y along the length x')
	plt.grid(True)
	plt.savefig("output_rod_500.png")
	plt.show()
	
	return X
	
		


def main():
	## A matrix in Ax = B
	### Problem -> 
	
	global Nx, delta_x
	Nx = 500
	delta_x = float(2)/Nx
	#print delta_x
	
	A = [[0 for x in xrange(int(Nx))] for x in xrange(int(Nx))]
	
	alpha = 2 + 3*(delta_x**2)
	#alpha2 = 1 + (x*delta_x)/2.0
	
	for x in xrange(1, Nx - 1):
		for y in xrange(x-1, x+2):
			if x == y:
				A[x][y] = -alpha
			elif y == x+1:
				value_x = (y)*delta_x - 1
				A[x][y] = 1 + (value_x*delta_x)/2.0
			elif y == x - 1: 
				value_x = (y+1)*delta_x - 1
				A[x][y] = 1 - (value_x*delta_x)/2.0
	A[0][0] = -alpha
	use1 = (1*delta_x) - 1
	#print use1
	A[0][1] = 1 + (use1*delta_x)/2.0
	
	use2 = ((Nx-1)*delta_x) - 1
	#print use2
	A[int(Nx)-1][int(Nx)-2] = 1 + (use2*delta_x)/2.0
	A[int(Nx)-1][int(Nx)-1] = -alpha 
	
			
	B = [0 for x in xrange(Nx)]
	
	for i in xrange(Nx):
		use_var = (i+1)*delta_x - 1
		B[i] = 6*(delta_x**2)*use_var
	
	B[0] += (1 + (delta_x/2.0))
	B[Nx - 1] -= (1 + (delta_x/2.0))
	
	#print B	
	
	## B matrix in Ax = B
	

	print "\n"
	#print "Solution:", jacobian(A, B), "\n\n"
	y = gauss_seidel(A, B)
	print "Solution:", y, "\n\n"	
	
	#print x
	
	'''points = []
	for as_point in xrange(Nx):
		points.append(as_point*delta_x)
	
	print "Length of list", len(XX)
	
	fig = plt.figure()
	ax = fig.gca(projection='3d')

	xx_index = 1
	for list1 in XX:
		ax.plot(points, list1, xx_index)
		xx_index += 1
		
	ax.plot(points, y, xx_index, label='Linear Solution')
	
	ax.set_xlabel('Length')
	ax.set_ylabel('Temperature')
	ax.set_zlabel('Iterations')
	ax.set_title('Temperature variation along the length of the rod')

	#plt.savefig("output_final3.png")
	ax.legend()

	plt.show()'''
	
	return 2


if __name__ == "__main__":
	sys.exit(main())
