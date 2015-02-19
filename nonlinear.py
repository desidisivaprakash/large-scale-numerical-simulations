'''siva'''

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
	sample= [300 for x in xrange(len(a))]
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
	
	
	

def jacobi(a, b):
	X = initial_guess(a)
	condition = True
	
	count = 0
	
	while condition == True:
		
		new_X = [0 for i in xrange(len(X))]
		for i in xrange(len(X)): 
			sum = 0
			for j in xrange(len(X)):
				
				if j != i:
					sum += (a[i][j])*(X[j])
							
			new_X[i] = (1.0/a[i][i])*(b[i] - sum)
		
		condition = condition_check(new_X, X)
		count += 1
		X = new_X
		
	print "Total iterations for solving equations by Jacobi method:", count
	return X

			
			
			

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
	
	
	

def sor(a, b):
	
	weights = []
	iterations = []
	
	for weight in drange(1.1, 1.99, 0.01):
		#print weight
		
		X = initial_guess(a)
		condition = True
	
		count3 = 0
		
		weights.append(weight)
		while condition == True:
		
			prev_X = copy.deepcopy(X)
			for i in xrange(len(X)):
			
				sum = 0
				for j in xrange(len(X)):
					
					if j != i:
						sum += (a[i][j])*(X[j])
								
				X[i] = (weight)*(1.0/a[i][i])*(b[i] - sum) + (1 - weight)*(X[i])
			
			condition = condition_check(prev_X, X)
	
			count3 += 1	
			
		#print "Total iterations for solving equations by SOR method for weight", weight, ":", count3
		#print X
		iterations.append(count3)
	
	minimum = iterations[1] 
	for p in xrange(1, len(iterations)):
		temp = iterations[p]
		
		if temp < minimum:
			minimum = temp
			index = p
			
	min_iter = min(iterations)
	print "Total iterations for solving equations by SOR method for optimum weight", weights[index], ":", iterations[index]
	#print "assert: it is equal to:", min_iter
	
	
	plt.plot(weights, iterations)
	plt.xlabel('Weight assigned to Gauss Seidel method')
	plt.ylabel('Iterations for reaching optimum solution')
	plt.title('Iterations v/s Weight analysis for SOR method')
	plt.grid(True)
	plt.savefig("output_SOR.png")
	plt.show()
	
	return 2





def conduction(a, b, beta):
	X = initial_guess(a)
	condition = True
	
	#count3 = 0
	weight = 1.92
	iteration = 1
	master_X = []
	
	while condition == True:
		print iteration
		iteration += 1
		prev_X = copy.deepcopy(X)
		
		# Improving B
		b[0] = beta -  T0
		b[-1] = beta - T10
		for i in xrange(1, len(b) - 1):
			b[i] = beta + sigma*(delta_x**2)*(prev_X[i]**4)
		
		for i in xrange(len(X)):
		
			sum = 0
			for j in xrange(len(X)):
				
				if j != i:
					sum += (a[i][j])*(X[j])
							
			X[i] = (weight)*(1.0/a[i][i])*(b[i] - sum) + (1 - weight)*(X[i])
		
		condition = condition_check(prev_X, X)
		
		master_X.append(prev_X)
		if condition == False:
			master_X.append(X)
	return master_X	
	
	
		


def main():
	## A matrix in Ax = B
	### Problem -> 
	
	global Nx, delta_x, sigma, T0, T10 
	Nx = 200
	delta_x = float(10)/Nx
	
	t_air = 200
	h = 0.05
	sigma = 2.7e-8
	
	#T = [0 for x in xrange(int(Nx))]
	
	T0 = 300
	T10 = 400
	
	A = [[0 for x in xrange(int(Nx))] for x in xrange(int(Nx))]
	
	alpha = 2 + (0.05)*(delta_x**2) 
	
	list1 = [1, -alpha, 1]
	A[0][0] = -alpha
	A[0][1] = 1
	A[int(Nx)-1][int(Nx)-2] = 1
	A[int(Nx)-1][int(Nx)-1] = -alpha 
	
	for x in xrange(1, int(Nx)-1):
		list2 = copy.deepcopy(list1)
		for y in xrange(x-1, int(Nx)):
			if list2:
				A[x][y] = list2.pop()
			
	#print A	
	B = [0 for x in xrange(Nx)]
	B[0] = -h*t_air*(delta_x**2) - T0
	B[-1] = -h*t_air*(delta_x**2) - T10
	
	for i in xrange(1, len(B)-1):
		B[i] = -h*t_air*(delta_x**2)
	
	#print B	
	
	beta = -h*t_air*(delta_x**2) - sigma*(t_air**4)*(delta_x**2)
	## B matrix in Ax = B
	

	print "\n"
	#print "Solution:", jacobi(A, B), "\n\n"
        #y = gauss_seidel(A, B)
	#y=jacobi(A,B)
	y=sor(A,B)
	print "Solution:", y, "\n\n"
	#useless_var = sor(A, B)
	XX = conduction(A, B, beta)	
	
	#print x
	
	points = []
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

	plt.show()
	
	return 2


if __name__ == "__main__":
	sys.exit(main())
