
import math

def divisors(n):
	divs = [1]
	for i in xrange(2, int(math.sqrt(n)) + 1):
		if (n % i) == 0:
			divs.append(i)
			if not i ** 2 == n:
				divs.append(n / i)
	divs.sort()
	return divs

abundant = []
abundantsums = {}
n = 28124

for i in xrange(1, n):
	if sum(divisors(i)) > i:
		abundant.append(i)
		for j in abundant:
			abundantsums[i + j] = 0
print "Almost There"
total = 0
for i in xrange(1, n):
	if not i in abundantsums:
		total += i
print total