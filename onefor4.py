
'''
Write a method to decide if two strings are anagrams or not

'''

def areanagrams(string1,string2):
	my_list1 = list(set(list(string1)))
	my_list1.sort()
	my_list2 = list(set(list(string2)))
	my_list2.sort()

	if my_list1 == my_list2:
		return True
	else:
		return False