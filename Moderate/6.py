#Given two arrays of integers, computethe pair of values (one value in each array) with the smalles (non-negative) difference. 
#Return the difference

import unittest

arr1 = [1,3,15,11,2]
arr2 = [23,127,235,19,8]

class numlist(object):
	def __init__(self, arg1, arg2):
		self.num = arg1
		self.team = arg2

def processList(ls, team):
	new_ls = []
	for index in range(len(ls)):
		#create object
		#insertion sort into list 
		if 

def smallestDiff(arr1, arr2):
	min_diff = 1000000
	last_diff = 0 
	pointer1 = 0
	pointer2 = 0 
	arr1 = arr1.sort()
	arr2 = arr2.sort()
	toggle = True

	while pointer1 <= len(arr1) && pointer2 <= len(arr2)

		current_diff = abs(arr1[pointer1] - arr2[pointer2])

		if current_diff < min_diff:
			min_diff = current_diff

		if last_diff < current_diff:
			if toggle:
				pointer1+=1
			else:
				pointer2+=1
		else:
			if toggle:
				pointer2+=1
			else:
				pointer1+=1
		last_diff = current_diff


class TestSmallestDiff(unittest.TestCase):
	"""docstring for TestSmallestDiff"""
	def test_one(self):
		self.assertEqual( smallestDiff(arr1,arr2),'10' )
		

if __name__ == '__main__':
	unittest.main()