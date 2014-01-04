
def getpents(n):
	p = [1]
	l = {}
	for i in xrange(1,n):
		l[getp(i)] = i
	return l

def getp(n):
	return (n * ((3 * n) - 1)) / 2

def checkem(ind, dep):
	global pentagonals
	pairs = []
	for i in xrange(1,ind):
		for j in xrange(100,dep):
			a = getp(i)
			b = getp(i+j)
			if (a + b) in pentagonals and abs(a-b) in pentagonals:
				pairs.append(i)
				pairs.append(j)
				pairs.append(a)
				pairs.append(b)
				pairs.append(b-a)
	return pairs

maxone = 50 * 1000
pentagonals = getpents(maxone)
maxpent = getp(maxone)

print checkem(10000,5000)
#[1560090, 7042750, 5482660]
#[Finished in 830.0s]
#  prAmEtuhA8
