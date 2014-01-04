
def factorial(n):
	if n < 2:
		return 1
	p = n
	while n > 1:
		n -= 1
		p *= n
	return p

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

def get_primes(max_number):
	known_composites = {}
	i = 2
	while i < max_number:
		if not i in known_composites:
			yield i
			known_composites[i*i] = [i]
		else:
			for j in known_composites[i]:
				known_composites.setdefault(i + j, []).append(j)
			del known_composites[i]
		i += 1

def checkprime(n):
	for i in get_primes(n**.5)

num = range(3)
num.pop(0)
print num

biggest = 0

for i in xrange(factorial(len(num))):
	c = undigitize(num)
	checkprime