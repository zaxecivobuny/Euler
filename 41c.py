#miraculously returns right answer in just over two minutes
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

def checkpandigital(n):
	temp = digitize(n)
	temp.sort()
	for i in range(len(temp)):
		if not temp[i] == i + 1:
			return False
	return True

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

largest = 0

for prime in get_primes(7654321):
	if checkpandigital(prime):
		largest = prime

print largest