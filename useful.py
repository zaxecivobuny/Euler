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

def checkprime(n):
	a = 0.0
	a = n ** .5
	if n < 2:
		return False
	for i in get_primes(int(a) + 1):
		if n % i == 0:
			return False
	return True

def digitize(n):
	a = str(n)
	b = []
	for i in a:
		b.append(int(i))
	return b

def undigitize(l):
	temp = l[:]
	n = temp.pop()
	place = 10
	while len(temp) >= 1:
		n += (temp.pop() * place)
		place *= 10
	return n

def factorial(n):
	if n < 2:
		return 1
	p = n
	while n > 1:
		n -= 1
		p *= n
	return p
