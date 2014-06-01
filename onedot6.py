'''

Given an image represented by an NxN matrix, where each pixel in the image is
Demonstrated with the examle of a square martrix

'''
my_list = []
my_rotated_list = []
n = 10

for i in range(0,n):
	my_list.append([j**i for j in range(0,n)])

for i in range(0,n):
	row = []
	for j in range(0,n):
		row.append(my_list[j][i])
	my_rotated_list.append(row)

print my_rotated_list


