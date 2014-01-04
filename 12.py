
import math

def primefactor(n):
	factors = []
	while n>1:
		i=2
		while i<=n:
			if n%i == 0:
				factors.append(i)
				n = n/i
				break
			i+=1
	return factors

def divisors(n):
	divs = []
	for i in xrange(1, int(math.sqrt(n)) + 1):
		if (n % i) == 0:
			divs.append(i)
			divs.append(n / i)
	divs.sort()
	return divs

triangle = 1
count = 1

while len(divisors(triangle)) < 500:
	count += 1
	triangle += count


print triangle
#print divisors(triangle)
