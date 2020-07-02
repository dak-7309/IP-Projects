#Name: Daksh Thapar
#Roll no: 2018137
#Section: A
#Group: 1

import matplotlib.pyplot as plt
import math
from copy import *

plt.ion()

def distance(point1,point2):									#this function calculates distance between two points, used here to obtain major and minor radii
	return math.sqrt( (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)



def transpose(X):												#this function calculates transpose of a matrix
	result=[]

	for i in range(len(X[0])):
		result.append([])

	for i in range(len(X[0])):
		for j in range(len(X)):
			result[i].append(0)

	for i in range(len(X)):
	   for j in range(len(X[0])):
	       result[j][i] = X[i][j]

	return result



def matrix_mult(A,B):											#used to multiply two matrices
	rows_A=len(A)
	rows_B=len(B)
	col_A=len(A[0])
	col_B=len(B[0])	
	pro=[]

	for i in range(rows_A):
		pro.append([])
	for i in range(rows_A):
		for j in range(col_B):
			pro[i].append(0)

	for i in range(rows_A): 
		for j in range(col_B): 
			for k in range(rows_B): 
				pro[i][j] += A[i][k] * B[k][j]   
	return pro

'''these functions give the necessary linear transformations that can be applied to coordinates to obtain new coordinates after the transformation is applied'''

def transform_scale(x,y):
	return [[x,0,0],[0,y,0],[0,0,1]]

def transform_rotate(angle):
	theta=math.radians(angle)
	sin=math.sin(theta)
	cos=math.cos(theta)
	return [[cos,-sin,0],[sin,cos,0],[0,0,1]]
	
def transform_translate(x,y):
	return [[1,0,x],[0,1,y],[0,0,1]]


#these draw functions do the transformations on the original points and plot them on a scaled surface using matplotlib library

def draw_scale(LIST,query,a,b):
	SM=[]
	new_list=[]
	for i in range(len(LIST)):			
		x=(matrix_mult(transform_scale(float(query[1]),float(query[2])), transpose([LIST[i]]) ))
		x=(transpose(x))
		new_list.append(x[0])
		SM.append(x[0][:2])

	p = plt.Polygon(SM, facecolor='none',edgecolor='r')
	plt.gca().add_patch(p)
	plt.axis('scaled')
	plt.pause(0.001)

	for i in range(len(new_list)):
		for j in range(len(new_list[i])):
			new_list[i][j]=round(new_list[i][j],3)
	return new_list
	
def draw_rotate(LIST,query,a,b):
	RM=[]
	new_list=[]
	for i in range(len(LIST)):			
		x=(matrix_mult(transform_rotate(float(query[1])), transpose([LIST[i]]) ))
		x=(transpose(x))
		new_list.append(x[0])
		RM.append(x[0][:2])

	p = plt.Polygon(RM, facecolor='none',edgecolor='r')
	plt.gca().add_patch(p)
	plt.axis('scaled')
	plt.pause(0.001)
	for i in range(len(new_list)):
		for j in range(len(new_list[i])):
			new_list[i][j]=round(new_list[i][j],3)

	return new_list
	
def draw_translate(LIST,query,a,b):
	TM=[]
	new_list=[]
	for i in range(len(LIST)):			
		x=(matrix_mult(transform_translate(float(query[1]),float(query[2])), transpose([LIST[i]]) ))
		x=(transpose(x))
		new_list.append(x[0])
		TM.append(x[0][:2])

	p = plt.Polygon(TM, facecolor='none',edgecolor='r')
	plt.gca().add_patch(p)
	plt.axis('scaled')
	plt.pause(0.001)
	for i in range(len(new_list)):
		for j in range(len(new_list[i])):
			new_list[i][j]=round(new_list[i][j],3)
	return new_list


#this is the menu for the user
n=input()

#for polygon,takes lists as input for coordinates, returns lists of new x and y coordinates
if n.lower()=='polygon':
	X=list(map(float,input().split()))
	Y=list(map(float,input().split()))
	LIST=[]
	lt=[]

	for i in range(len(X)):
		LIST.append([round(X[i],3),round(Y[i],3),1])
		lt.append([round(X[i],3),round(Y[i],3)])
	p = plt.Polygon(lt, facecolor='none',edgecolor='r')
	plt.gca().add_patch(p)
	plt.axis('scaled')
	plt.pause(0.001)
	
	while True:	
		query=list(input().split())
		if query[0]=='quit':
			break
		else:
			if query[0]=='S':			#S is for scaling transformation
	
				LIST=draw_scale(LIST,query,0,0)
				X_new=[]
				Y_new=[]

				for i in range(len(LIST)):
					X_new.append(LIST[i][0])
					Y_new.append(LIST[i][1])
				print(*X_new)
				print(*Y_new)

			if query[0]=='R' :			#R is for rotation transformation
					
				LIST=draw_rotate(LIST,query,0,0)
				X_new=[]
				Y_new=[]

				for i in range(len(LIST)):
					X_new.append(LIST[i][0])
					Y_new.append(LIST[i][1])
				print(*X_new)
				print(*Y_new)
	
			if query[0]=='T' :			#T is for translation transformation
				
				LIST=draw_translate(LIST,query,0,0)
				X_new=[]
				Y_new=[]

				for i in range(len(LIST)):
					X_new.append(LIST[i][0])
					Y_new.append(LIST[i][1])
				print(*X_new)
				print(*Y_new)
				
#for disc, takes center (x and y coord.) and radii (both major and minor) as input, returns new center and radii

if n.lower()=='disc':

	a,b,r1,r2=list(map(float,(input().split())))
	x=0
	LIST=[]
	lt=[]
	for i in range(1000):
		x+=0.00628318530717958647692428676655
		LIST.append([a+r1*math.cos(x),b+r2*math.sin(x),1])
		lt.append([a+r1*math.cos(x),b+r2*math.sin(x)])


	center=[a,b,1]
	p = plt.Polygon(lt, facecolor='none',edgecolor='r')
	plt.gca().add_patch(p)
	plt.axis('scaled')
	plt.pause(0.001)

	while True:
		query=list(input().split())
		if query[0]=='quit':
			break
		else:
			if query[0]=='S':					#S is for scaling transformation
				LIST=draw_scale(LIST,query,a,b)
								
				center=(matrix_mult(transform_scale(float(query[1]),float(query[2])), transpose([center]) ))
				center=(transpose(center))
				center=center[0]
				for i in range(len(center)):
					center[i]=round(center[i],2)

				dist=[]
				for i in range(len(LIST)):
					dist.append(distance(LIST[i][:2], center[:2]))



				print(*center[:2],round(max(dist),2),round(min(dist),2))

			if query[0]=='R' :					#R is for rotation transformation
				LIST=draw_rotate(LIST,query,a,b)

				center=(matrix_mult(transform_rotate(float(query[1])), transpose([center]) ))
				center=(transpose(center))
				center=center[0]
				for i in range(len(center)):
					center[i]=round(center[i],2)
				
				dist=[]
				for i in range(len(LIST)):
					dist.append(distance(LIST[i][:2], center[:2]))

				print(*center[:2],round(max(dist),2),round(min(dist),2))
				
			if query[0]=='T' :					#T is for translation transformation
				LIST=draw_translate(LIST,query,a,b)

				center=(matrix_mult(transform_translate(float(query[1]),float(query[2])), transpose([center]) ))
				center=(transpose(center))
				center=center[0]
				for i in range(len(center)):
					center[i]=round(center[i],2)
				dist=[]
				for i in range(len(LIST)):
					dist.append(distance(LIST[i][:2], center[:2]))

				print(*center[:2],round(max(dist),2),round(min(dist),2))
			