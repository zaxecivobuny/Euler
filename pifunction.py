from useful import get_primes

def prime_n(n):
	if n == 1:
		return 2
	pi = []
	while len(pi) < n:
		for i in get_primes(n * n):
			pi.append(i)
			if len(pi) == n:
				return pi[-1]

print prime_n(10*1000*1000)

