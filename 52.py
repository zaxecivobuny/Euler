from useful import digitize

def is_permute(x,y):
	a = digitize(x)
	b = digitize(y)
	a.sort()
	b.sort()
	return (a == b)

def maing():
	largest = 1000*1000
	for i in xrange(1,largest):
		sofarsogood = True
		for j in xrange(2,7):
			if not is_permute(i, j*i):
				sofarsogood = False
				break
		if sofarsogood == True:
			return i
	print "greater than", largest

print maing()