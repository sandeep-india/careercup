'''
Imagine a robot sitting on the upper left hand corner of an NxN grid The robot can only move in two directions: right and down How many possible paths are there for the robot?
FOLLOW UP
Imagine certain squares are “off limits”, such that the robot can not step on them Design an algorithm to get all possible paths for the robot

'''
from math import factorial

def gridmotion(n):
	if n == 1:
		return 2
	else:
		return (factorial(n*2) / factorial(n)**2) + gridmotion(n-1)

