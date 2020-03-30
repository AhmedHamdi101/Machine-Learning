import numpy as np 
from collections import deque
import copy
import time


class Tree(object):
    def __init__(self):
        self.data  = None
        self.parent = None
		
t1 = time.time()
d = dict()
goal = [[0, 1, 2], [3, 4, 5] , [6 , 7 , 8]]
intialState =np.array( [[8, 1, 3], [4, 2, 5] , [7 , 0 , 6]])
root = Tree()
root.data = intialState
stack = []
nodeExpanded = []
stack.append(root)
flag = 0



while len(stack) != 0:

	real = stack.pop()	
	nodeExpanded.append(real)
	b = np.argwhere(real.data == 0)
	flag = 0	
	print("-----------------------------")
	print(real.data)
	print("-----------------------------")
	
	#get the positon of the zero
	row = int(b[0][0]) 
	col = int(b[0][1]) 
	
	if  row == 0 :
		node = copy.deepcopy(real)
		node.data[row][col],node.data[row+1][col] = node.data[row+1][col],node.data[row][col]
		print(node.data)
		if str(node.data) in d:
			print("Duplicate")
		else:
			d[str(node.data)] = None
			node.parent = real
			stack.append(node)
	
	elif row == 2:
		node = copy.deepcopy(real)
		node.data[row][col],node.data[row-1][col] = node.data[row-1][col],node.data[row][col]
		print(node.data)
		if str(node.data) in d:
			print("Duplicate")
		else:
			d[str(node.data)] = None
			node.parent = real
			stack.append(node)
	
	elif  row == 1 :
		
		node = copy.deepcopy(real)
		node.data[row][col],node.data[row+1][col] = node.data[row+1][col],node.data[row][col]
		print(node.data)
		if str(node.data) in d:
			print("Duplicate")
		else:
			d[str(node.data)] = None
			node.parent = real
			stack.append(node)
			
		node = copy.deepcopy(real)
		node.data[row][col],node.data[row-1][col] = node.data[row-1][col],node.data[row][col]
		print(node.data)
		if str(node.data) in d:
			print("Duplicate")
		else:
			d[str(node.data)] = None
			node.parent = real
			stack.append(node)
			
	if col == 1: 
		
		node = copy.deepcopy(real)
		node.data[row][col],node.data[row][col+1] = node.data[row][col+1],node.data[row][col]
		print(node.data)
		if str(node.data) in d:
			print("Duplicate")
		else:
			d[str(node.data)] = None
			node.parent = real
			stack.append(node)
		
		node = copy.deepcopy(real)
		node.data[row][col],node.data[row][col-1] = node.data[row][col-1],node.data[row][col]
		print(node.data)
		if str(node.data) in d:
			print("Duplicate")
		else:
			d[str(node.data)] = None
			node.parent = real
			stack.append(node)
	elif col == 0:
		
		node = copy.deepcopy(real)
		node.data[row][col],node.data[row][col+1] = node.data[row][col+1],node.data[row][col]
		print(node.data)
		if str(node.data) in d:
			print("Duplicate")	
		else:
			d[str(node.data)] = None
			node.parent = real
			stack.append(node)
	
	elif col == 2 :
		node = copy.deepcopy(real)
		node.data[row][col],node.data[row][col-1] = node.data[row][col-1],node.data[row][col]
		print(node.data)
		if str(node.data) in d:
			print("Duplicate")
		else:
			d[str(node.data)] = None
			node.parent = real
			stack.append(node)
	
	if np.array_equal(real.data,goal):
		print("solution found")
		t2 = time.time()
		
		i = 0
		print ("the PATH IS")
		print (real.data)
		new = real.parent
		while new != None:
			print(" ")
			print(new.data)
			new = new.parent
			i = i+1
		print("cost = " + str(i) )
		print("Depth = " + str(i+1))
		print("node expanded " + str(len(nodeExpanded)))
		print ("running time: " + str(t2-t1))
		break
	
	if flag == 4:
		print("backing from the branch and entering next node")
	print("loop")

