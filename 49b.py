
def digitize(n):
	a = str(n)
	b = []
	for i in a:
		b.append(int(i))
	return b

def sortnumber(n):
	m = digitize(n)
	m.sort()
	return m

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

fourdigprimes = []
fourdigprimedict = {}

for i in get_primes(10000):
	if i > 1000:
		fourdigprimes.append(i)
		fourdigprimedict[i] = 0

most = len(fourdigprimes)
print most
testers = [0,0,0]

for i in fourdigprimes:
	if i > 3333:
		break
	for j in xrange(1, 3333):
		testers[0] = i
		testers[1] = i + j
		testers[2] = testers[1] + j
		if testers[2] > fourdigprimes[-1]:
			break
		elif testers[1] in fourdigprimedict and testers[2] in fourdigprimedict:
			if sortnumber(testers[0]) == sortnumber(testers[1]) == sortnumber(testers[2]):
				print testers

