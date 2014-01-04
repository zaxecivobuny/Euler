total = 5
count = 0

def countup(l):
	global count
	global total
	if sum(l) == total:
		count += 1 
l = xrange(7)

for a in xrange(0,total,1):
	l[0] = a
	for b in xrange(0,total,2):
		l[1] = b
		for c in xrange(0, total, 5):
			l[2] = c
			countup
		countup
	countup

print count