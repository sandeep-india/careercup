'''

Write a method to generate the nth Fibonacci number

'''

def fab(n):
	
	if n == 1 or n == 2:
		return 1
	else:
		return fab(n-1)+fab(n-2)

