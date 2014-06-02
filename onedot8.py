'''
Assume you have a method isSubstring which checks if one word is a substring of another 

'''

def isSubstring(s1,s2):
	len1 = len(s1)
	len2 = len(s2)
	if s2 > s1:
		return False
	else:
		for i in range(0,len1-len2+1):
			if s1[i:i+len2] == s2:
				return True

	return False

def rotation(s1,s2):
	new = s1+s1
	if len(s1) == len(s2):
 		return isSubstring(new,s2)
 	else: return False