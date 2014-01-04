
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

def isprime(n):
	m = 0.0
	m = n**.5
	for i in get_primes(int(m)):
		if (n % i) == 0:
			return False
	return True

def goldbach(n):

	for i in get_primes(n):
		for j in xrange(1, n):
			p = i + (2 * (j**2))
			if n == i + (2 * (j**2)):
				return True
	return False

c = 9

while True:
	if isprime(c):
		c += 2
		#print c
	else:
		if not goldbach(c):
			print c
			break
		c += 2

#halted in 860s
