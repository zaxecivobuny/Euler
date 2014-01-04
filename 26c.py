
def remainders(n):
	rlist = {}
	denominator = n
	numerator = 10
	while True:
		quotient = numerator / denominator
		remainder = numerator % denominator
		#print quotient
		#print remainder
		if remainder == 0:
			return 0
		elif remainder in rlist:
			break
		else:
			rlist[remainder] = 1
			numerator = remainder * 10
	#print rlist
	return len(rlist)

largest = 0
most = 0

for i in range(2, 1000):
	r = remainders(i)
	#print i, r
	most = max(most, r)
	if most == r:
		largest = i
		print r, i

print largest, most





