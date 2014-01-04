                                                 
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

def concatenum(*args):
	c = []
	for i in args:
		c += digitize(i)
	return undigitize(c)

def checkpandigital(l):
	temp = l[:]
	temp.sort()
	if not len(temp) == 9:
		return False
	for i in xrange(9):
		if not temp[i] == (i + 1):
			return False
	return True

largest = 0

for i in xrange(1, 1000 * 100):
	product = []
	count = 1
	while len(product) < 9:
		product += digitize(i * count)
		count += 1
	if checkpandigital(product):
		print i
		print product
		largest = max(undigitize(product),largest)

print largest



