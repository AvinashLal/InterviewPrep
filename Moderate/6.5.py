#number of ways to climb stair_height stairs with step_inc steps at a times 

num_way = {}
num_way[1], num_way[2]  = 1, 2

def num_ways(stair_height, step_inc):
	if stair_height <= 0:
		return 0
	if stair_height in num_way.keys():
		return num_way[stair_height]
	else:
		num_way[stair_height] = 0 
		for step in step_inc:
			num_way[stair_height] += num_way[stair_height-step] + step
		return num_way[stair_height]

print num_ways(3,[1,2])
