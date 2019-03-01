# Crime forcasting
# CS Freshman success community
# 3/11/17
# Team 2: Daniel Werminghausen

import sys

from data import *

def matrix(height, width):
	return [[0 for col in range(height)] for row in range(width)]
	

def matrixCalculation(fileName):
	TOP = 733940 
	LEFT = 7603950 
	CELL_SIZE = 250
	matrix2 = matrix(390, 331)
	# x = i
	# y = j
	# newMatrix = None

	with open(fileName) as f:
	    file = f.readlines()
	for line in file:
		x = line.split(',')[1]
		y = line.split(',')[2]
		i = int((TOP - int(y)) / CELL_SIZE)
	# i = int ((733,940 - 681,238) / 250) 
		j = int((int(x) - LEFT) / CELL_SIZE)
	# j= int((7,692,812 - 7,603,950) / 250)
		# print(j)
		if (0 <= i <= 331 and 0 <= j <= 390):
		# if (i > 331 or j > 390):
			# print(i, j)
			matrix2[i][j] += 1 	
				# [[i + 1 for i in j] for j in matrix2]
	return matrix2
		
# matrixCalculation('data.py')
# print(matrix(390, 331))


#saves result in result.txt
def save(file,data):
	f = open( file,'w')
	f.write(repr(data))
	f.close()
save("result.txt", matrixCalculation('data.py'))

