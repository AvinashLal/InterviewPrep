#How many ways to decipher code numerical to alphabetical code
import unittest

code = 129312943194

def ways_to_decipher(code, ind):
	str_num = 0 
	#pop character
	for index in range(ind, len(code) - 1):
		digit = code[index]
		next_digit = code[index + 1]

		if digit == 1:
			if next_digit == 0:
				return ways_to_decipher(code, index + 2) 
			else:
				return ways_to_decipher(code, index + 1) +  ways_to_decipher(code, index + 2)
		if digit == 2:
			if next_digit == 0:
				return ways_to_decipher(code, index + 2) 
			elif next_digit >=1 and <=6:
				return ways_to_decipher(code, index + 1) +  ways_to_decipher(code, index + 2)
			else: 
				return return ways_to_decipher(code, index + 1) 
		else:
			return ways_to_decipher
	#validate number 
	#add to sum

print ways_to_decipher(code, 0)

class TestFun(unittest.TestCase):
	"""docstring for ClassName"""
	def test_one(self):
		self.assertEqual(ways_to_decipher(code), '1')		

#if __name__ == '__main__':
#	unittest.main()