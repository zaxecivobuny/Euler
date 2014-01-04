
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

def getfracplace(n):
	n = n - 1 
	global frac
	global count
	while len(frac) <= n:
		d = digitize(count)
		frac += d
		count += 1
	return frac[n]


frac = []
count = 1
product = 1
tens = 1

for i in xrange(7):
	tens = 10 ** i
	print tens
	product *= getfracplace(tens)

print product

