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

def truncright(n):
	global primes
	temp = digitize(n)
	for i in xrange(len(temp)-1):
		temp.pop(0)
		if not undigitize(temp) in primes:
			return False
	return True

def truncleft(n):
	global primes
	temp = digitize(n)
	for i in xrange(len(temp)-1):
		temp.pop()
		if not undigitize(temp) in primes:
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

primes = {2:0, 3:0, 5:0, 7:0,}
leftandright = []

for i in get_primes(1000*1000):
	primes[i] = 0
	if i>10 and truncright(i) and truncleft(i):
		leftandright.append(i)

print leftandright
print len(leftandright)
print sum(leftandright)