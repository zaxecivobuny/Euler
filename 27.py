import math

def get_primes(max_number):
	known_composites = {}
	i = 2
	while i < max_number:
		if not i in known_composites:
			yield i
			known_composites[i*i] = [i]
		else:
			for j in known_composites[i]:
				known_composites.setdefault(i + j, []).append(j)
			del known_composites[i]
		i += 1

def prime(n):
	n = abs(n)
	if n <= 1:
		return False		
	for i in get_primes(int(math.sqrt(n))):
		if n % i == 0:
			return False
	return True

# function takes two arguments, then tests every number from zero on, until n^2 + a*n + b is composite
def quadratic_test(a,b):
	n = 0
	while True:
		x = ( n * ( n + a ) ) + b
		if not prime(x):
			return n 
		else:
			n += 1

most = 0
bestA = 0
bestB = 0
low = -999
high = 1000


for i in xrange(low, high):
	for j in get_primes(high):
		q = quadratic_test(i, j)
		most = max(q, most)
		if q == most:
			bestA = i
			bestB = j

print bestA
print bestB
print most
print bestA * bestB

#-61
#971
#71
#[Finished in 4117.1s]