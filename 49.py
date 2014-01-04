
def digitize(n):
	a = str(n)
	b = []
	for i in a:
		b.append(int(i))
	return b

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

for i in xrange(most):
	for j in xrange(2, 3333):
		for k in xrange(3):
			testers[k] = (j * k) + fourdigprimes[i]
		if testers[-1] in fourdigprimedict and testers[-2] in fourdigprimedict:
			checksout = True
			print "almost"
			for k in xrange(2):
				if not digitize(testers[k]).sort == digitize(testers[-1]).sort:
					checksout = False
			if checksout:
				print testers

