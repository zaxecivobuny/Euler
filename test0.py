
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

def quadratic_test(a,b):
	n = 0
	while True:
		x = ( n * ( n + a ) ) + b
		#print x
		#print prime(x)
		if not prime(x):
			return n 
		else:
			#print n
			#print x
			n += 1


print -61 * 971