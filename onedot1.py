'''
Implement an algorithm to determine if a string has all unique characters What if you can not use additional data structures?

'''

def unique_string(input_string):
	my_list=list(input_string)
	my_list1 = list(set(input_string))
	if len(my_list) > len(my_list1):
		return False
	return True

'''
With out using datastructures.

'''

def unique_str(input_string):
	length=len(input_string)
	unique = True
	for i in range(0,length):
		
		if (i>0):
			new_string = input_string[0:i]+input_string[i+1:length]
		else:
			new_string = input_string[1:length]

		if input_string[i] in new_string:
			unique = False

	return unique



