def primefactor(n):
	factors = []
	while n > 1:
		i = 2
		while i <= n:
			if n % i == 0:
				factors.append(i)
				n = n/i
				break
			else:
				i+=1
	return factors
	
mainfactors = primefactor(600851475143)
print mainfactors
print mainfactors[-1]