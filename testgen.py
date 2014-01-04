import math

def heneral(m):
	i = 1
	while i <= m:
		yield i
		i +=1

def get_primes(max_number):
	known_composites = {}
	for i in xrange(2, max_number):
		if not i in known_composites:
			yield i
			known_composites[i*i] = [i]
		else:
			for j in known_composites[i]:
				known_composites.setdefault(i + j, []).append(j)
			del known_composites[i]




total = 0
for primes in get_primes(10):
	total += primes
print total