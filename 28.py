
spiral_size = 1001 * 1001
level = 1
total = 1
count_in_level = 1
i = 3
while i <= spiral_size:
	total += i
	count_in_level += 1
	if count_in_level > 4:
		count_in_level = 1
		level += 1
	i += level * 2	
	
print total
	

