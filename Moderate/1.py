#write a function to swap a number in place 

def swapinplace(a, 	b):
	a = a - b 
	b = a + b
	a = b - a
	print (a,b)  

swapinplace(257,1456)