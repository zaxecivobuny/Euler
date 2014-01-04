import math

for a in xrange(2, 997):
	for b in xrange(a, 998):
		c = math.sqrt((a**2)+(b**2))
		if ((a + b) + c) == 1000:
			print a
			print b
			print c
			print a * b * c
			