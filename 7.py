
primes = [2]

count = 3

while len(primes) < 10001:
	isprime = True
	for prime in primes:
		if (count % prime) == 0:
			isprime = False
			break
	if isprime:
		primes.append(count)
	count += 2

print primes[-1]	