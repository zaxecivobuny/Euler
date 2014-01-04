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

def rotate(l):
	temp = l[:]
	first = temp[0]
	for i in range(len(temp) - 1):
		temp[i] = temp[i + 1]
	temp[-1] = first
	return temp

def rotations(n):
	global primes
	l = digitize(n)
	checker = rotate(l)
	for i in range(len(l)):
		if not undigitize(checker) in primes:
			return False
		checker = rotate(checker)
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

primes = {}
circular = []
for i in get_primes(1000*1000):
	primes[i] = 0
	if i < 10:
		circular.append(i)
	elif rotations(i):
		m = i
		for j in range(len(digitize(i))):
			circular.append(m)
			m = undigitize(rotate(digitize(m)))
			if m == circular[-1]:
				break

print circular
print len(circular)
