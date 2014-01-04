# takes 600 seconds to halt
def checkpandigital(a, b, c):
	d = str(a) + str(b) + str(c)
	if not len(d) == 9:
		return False
	x = []
	for i in d:
		x.append(int(i))
	x.sort()
	for i in xrange(9):
		if not x[i] == (i + 1):
			return False
	return True

def getpandigital():
	allofem = {}
	for i in xrange(2, 98765):
		for j in xrange(3, 10 ** ( 7 - len( str(i) ) ) ):
			k = i * j
			if checkpandigital(i,j,k):
				allofem[k] = [i,j]
	print allofem
	return sum(allofem)

print getpandigital()
