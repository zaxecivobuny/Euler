
import math

def divisors(n):
	divs = []
	for i in xrange(1, int(math.sqrt(n)) + 1):
		if (n % i) == 0:
			divs.append(i)
			divs.append(n / i)
	divs.sort()
	return divs

def sumdivisors(n):
	d = divisors(n)
	d.pop()
	total = 0
	for i in d:
		total += i
	return total

amicable = {}

for i in range(1, 10 * 1000):
	if (not sumdivisors(i) == i) and sumdivisors(sumdivisors(i)) == i:
		amicable[i] = [sumdivisors(i)]
		amicable[sumdivisors(i)] = i

print sum(amicable)