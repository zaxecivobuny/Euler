
def checkprime(n):
	a = 0.0
	a = n ** .5
	for i in get_primes(int(a)):
		if n % i == 0:
			return False
	return True

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

def countprimefactors(n):
	rem = n
	cap = 0.0
	cap = n ** .5
	count = 0
	for i in get_primes(n):
		if i > cap and count == 0:
			return 0
		if rem % i == 0:
			count += 1
		while rem % i == 0:
			rem /= i
		if rem < 2:
			break
	return count

distinct = 4

a = 1
# 53000

while True:
	checker = True
	for i in xrange(distinct):
		if not countprimefactors(a+i) == distinct:
			checker = False
			break
	if checker:
		print a
		break
	
	a += 1
	
# 134043