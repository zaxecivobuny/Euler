#takes 209 seconds

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

def factorial(n):
	if n < 2:
		return 1
	p = n
	while n > 1:
		n -= 1
		p *= n
	return p

def checkdiv(n):
	c = [2,3,5,7,11,13,17]
	temp = n[:]
	for i in range(7):
		if not undigitize(temp[i+1:i+4]) % c[i] == 0:
			return False
	return True

def iterate(l):
	for i in range(len(l)):
		n = len(l) - i -1
		if l[n] > l[n - 1]:
			tempfront = l[:n-1]
			tempback = l[n-1:]
			holder = tempback[0]
			tempback.sort()
			for j in xrange(len(tempback)):
				if tempback[j] > holder:
					tempfront.append(tempback.pop(j))
					break
			return tempfront + tempback
	return l	

m = range(10)
listall = []

for i in range(factorial(10)):
	if checkdiv(m):
		listall.append(undigitize(m))
	m = iterate(m)

print listall
print sum(listall)