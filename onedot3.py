'''
Remove duplicate chars in a string.

'''
def unique_str(input_string):
	length=len(input_string)
	final_string = ''
	buffer_char = ''
	for i in range(0,length):

		if (i>0):
			new_string = input_string[0:i]+input_string[i+1:length]
		else:
			new_string = input_string[1:length]

		if input_string[i] in new_string:
			if input_string[i] in buffer_char:
				pass
			else:
				buffer_char += input_string[i]
				final_string += input_string[i]
				print final_string
		else:
			final_string += input_string[i]
			print final_string

	return final_string

'''

Test cases
"aabbccdd"
"aaabbbcccddd"
"abcdabcdabcd"

'''
