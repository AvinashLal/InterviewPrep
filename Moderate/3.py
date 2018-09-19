#Given two line segments(represented as start and end point) 
#compute the point of intersection, if any 
import unittest

line1 = [(1,1),(2,3)]
line2 = [(2,2), (3,4)]
line3 = [(0,0),(2,3)]

def equationFinder(line):
	point1, point2  = line[0], line[1]
	x1, y1 = point1 
	x2, y2 = point2 
	slope = (y2 - y1)/(x2 - x1)
	yIntercept = y1 - slope*x1
	return (slope, yIntercept)

def intersectionPoint(line1, line2):
	#find equations of lines
	slope1, yIntercept1 = equationFinder(line1)
	slope2, yIntercept2 = equationFinder(line2)
	print slope2
	if slope1 == slope2: 
		if yIntercept1 == yIntercept2:
			return 'same line'
		else:
			return 'parallel'
	else:
		x = (yIntercept1 - yIntercept2)/(slope2 - slope1)
		print slope2, yIntercept2
		y = x * slope1 + yIntercept1
		return str(x) + ','+ str(y)

print intersectionPoint(line1, line3)