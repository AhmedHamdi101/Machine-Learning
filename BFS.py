import numpy as np 
from collections import deque
import copy
import time
#creat the class that we will use
class Tree(object):
    def __init__(self):
        self.data  = None
############################################
#parent pointer to use it later get the path of the goal
        self.parent = None	
############################################

t1 = time.time()
#intialize the 	queue
queue =deque()

############################################
#intilalize stack to save the nodes we expand
nodeExpanded = []
############################################

#a hashmap to make sure nodes dosen't repeat in the tree 
d = dict()

#the goal matrix
goal = [[0, 1, 2], [3, 4, 5] , [6 , 7 , 8]]

#intialize the first node
root = Tree()

#np.array help to use the np functions later, like getting the position
intialState =np.array( [[8, 2, 3], [4, 1, 7] , [0 , 5 , 6]])

#store data in the node
root.data = intialState

#store node in the queue
queue.append(root)

while len(queue) != 0:
	#get the data
	real = queue.popleft()
	
	#################################
	#each node we get out of the queue we save into the stack 
	#last node in the satck is the solution
	nodeExpanded.append(real)
	#################################
	
	#print the first node in each iteration
	print("----------------------")
	print(real.data)
	print("----------------------")
	
	#using np to get the 0 position
	b = np.argwhere(real.data == 0)
	
	#putting them in values to use them in it conditions
	row = int(b[0][0]) 
	col = int(b[0][1]) 
	
	#if 0 was in row zero we go down
	if  row == 0 :
		temp = copy.deepcopy(real)
		temp.data[row][col],temp.data[row+1][col] = temp.data[row+1][col],temp.data[row][col]
		print(temp.data)
		#check if the solution was already in dict("d")
		if str(temp.data) in d:
			print("duplicate")
		else:
			#convert matrix into string and store it as key in dict("d")
			d[str(temp.data)] = None
			#store in queue
			temp.parent = real
			queue.append(temp)
	
	#if 2 was in row zero we go up		
	elif row == 2:
		temp = copy.deepcopy(real)
		temp.data[row][col],temp.data[row-1][col] = temp.data[row-1][col],temp.data[row][col]
		print(temp.data)
		if str(temp.data) in d:
			print("duplicate")
		else:
			d[str(temp.data)] = None
			temp.parent = real
			queue.append(temp)
			
	#if row was 1 we go and down
	elif  row == 1 :
		
		#down
		temp = copy.deepcopy(real)
		temp.data[row][col],temp.data[row+1][col] = temp.data[row+1][col],temp.data[row][col]
		print(temp.data)
		if str(temp.data) in d:
			print("duplicate")
		else:
			d[str(temp.data)] = None
			temp.parent = real
			queue.append(temp)
		
		#then up
		temp = copy.deepcopy(real)
		temp.data[row][col],temp.data[row-1][col] = temp.data[row-1][col],temp.data[row][col]
		print(temp.data)
		if str(temp.data) in d:
			print("duplicate")
		else:
			d[str(temp.data)] = None
			temp.parent = real
			queue.append(temp)
	#if col = 1 we go left and right
	if col == 1: 		
		#right
		temp = copy.deepcopy(real)
		temp.data[row][col],temp.data[row][col+1] = temp.data[row][col+1],temp.data[row][col]
		print(temp.data)
		if str(temp.data) in d:
			print("duplicate")
		else:
			d[str(temp.data)] = None
			temp.parent = real
			queue.append(temp)
		#then left
		temp = copy.deepcopy(real)
		temp.data[row][col],temp.data[row][col-1] = temp.data[row][col-1],temp.data[row][col]
		print(temp.data)
		if str(temp.data) in d:
			print("duplicate")
		else:
			d[str(temp.data)] = None
			temp.parent = real
			queue.append(temp)
	#if col = 0 we go left		
	elif col == 0:
		temp = copy.deepcopy(real)
		temp.data[row][col],temp.data[row][col+1] = temp.data[row][col+1],temp.data[row][col]
		print(temp.data)
		if str(temp.data) in d:
			print("duplicate")
		else:
			d[str(temp.data)] = None
			temp.parent = real
			queue.append(temp)
	#if col = 2 we go right		
	elif col == 2 :   
		temp = copy.deepcopy(real)
		temp.data[row][col],temp.data[row][col-1] = temp.data[row][col-1],temp.data[row][col]
		print(temp.data)
		if str(temp.data) in d:
			print("duplicate")
		else:
			d[str(temp.data)] = None
			temp.parent = real
			queue.append(temp)
	#check if the solution was found		
	if np.array_equal(real.data,goal):
		print("solution found")
		t2 = time.time()
		######################################
		#loop to check parent pointer from goal to root
		#and get the depth
		i = 0
		print ("the PATH IS")
		print (real.data)
		new = real.parent
		while new != None:
			print(new.data)
			new = new.parent
			i = i+1
		print("cost = " + str(i) )
		print("Depth = " + str(i+1))
		print("node expanded"+ str(len(nodeExpanded)))
		print ("running time :" + str(t2-t1))
		######################################
		
		break
	
		