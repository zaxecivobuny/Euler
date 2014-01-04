def checkpalindrome(n):
	temp = digitize(n)
	for i in xrange(len(temp)/2):
		if not temp[i] == temp[-1 * (i + 1)]:
			return False
	return True

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

def basetwo(n):
	temp = n
	place = 1
	new = []
	while place <= temp:
		place *= 2
	while place >= 1:
		if place <= temp:
			new.append(1)
			temp -= place
			place /= 2
		else:
			place /= 2
			new.append(0)
	return undigitize(new)

dbldrome = []

for i in xrange(1, 1000*1000):
	if checkpalindrome(i) and checkpalindrome(basetwo(i)):
		dbldrome.append(i)

#print dbldrome
print len(dbldrome)
print sum(dbldrome)



