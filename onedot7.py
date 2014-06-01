'''
Write an algorithm such that if an element in an MxN matrix is Zero, its entire row and column is set to Zero.

'''

def zerofy(my_list):
	rows=len(my_list)
	columns =len(my_list[0])
	row_list = []
	column_list = []
	for i in range(0,rows):
		for j in range(0,columns):
			if my_list[i][j] == 0:
				if not i in row_list:
					row_list.append(i)
				if not j in column_list:
					column_list.append(j)

	for i in range(0,rows):
		if i in row_list:
			for j in range(0,columns):
				my_list[i][j] = 0

	for j in range(0,columns):
		if j in column_list:
			for i in range(0,rows):
				my_list[i][j] = 0

	return my_list

	