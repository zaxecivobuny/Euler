def lcd(n,d):
	a = n
	b = d
	counter = 2
	while counter <= min(a,b):
		if (a % counter) == 0 and (b % counter) == 0:
			a /= counter
			b /= counter
		else:
			counter += 1
	return b	


def divisor(n, d):
	c = checkreduce(n, d)
	if c == 0:
		return 0
	if not ( n % c == d % c == 0 ):
		return 0
	else:
		return c


def checkreduce(n, d):
	n0 = str(n)
	d0 = str(d)
	n1 = []
	d1 = []
	for i in range(2):
		n1.append(int(n0[i]))
		d1.append(int(d0[i]))
	c = 0
	for i in n1:
		for j in d1:
			if i == j:
				c = i
	if c > 1:
		if not n1[0] == c:
			a = n1[0]
		else:
			a = n1[1]
		if not d1[0] == c:
			b = d1[0]
		else:
			b = d1[1]
		if a ==0 or b == 0:
			return 0
		x = 0.0
		y = 0.0
		x += a
		y += n
		x /= b
		y /= d
		if x == y:
			return c
	else:
		return 0

listnums = []
listdenoms = []


print checkreduce(49,98)

for i in xrange(10, 98):
	for j in xrange(i+1, 99):
		k = checkreduce(i, j)
		if k > 1:
			listnums.append(i)
			listdenoms.append(j)
print listnums
print listdenoms

bignum = 1
for i in listnums:
	bignum *= i
bigdenom = 1
for i in listdenoms:
	bigdenom *= i

print bignum, bigdenom, lcd(bignum, bigdenom)

#for i in range(4):
#	print listnums(i), "/" 


