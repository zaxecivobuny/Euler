s = {}
x = 2
y = 101

for a in xrange(x,y):
	for b in xrange(x,y):
		s[a ** b] = 0

print len(s)