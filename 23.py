
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

for i in xrange(1, 28124):
	if sum(divisors(i)) > i:
		abundant.append(i)

abundantsums = {}

for i in abundant:
	for j in abundant:
		abundantsums[i + j] = 0

total = 0

for i in xrange(1, 28124):
	if not i in abundantsums:
		total += i

print total