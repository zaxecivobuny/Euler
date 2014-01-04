
def factorial(n):
	if n == 0:
		return 1
	x = n
	while x > 2:
		x -= 1
		n *= x
	return n

def combinatori(n,r):
	a = factorial(n)
	b = factorial(r) * factorial(n - r)
	return a/b

count = 0

for n in xrange(1,101):
	for r in xrange (1, n + 1):
		if combinatori(n,r) > (1000 * 1000):
			count += 1 

print count



