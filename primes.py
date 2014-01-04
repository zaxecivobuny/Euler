import math

def primefactor(n):
	factors = []
	while n>1:
		i=2
		while i<=n:
			if n%i == 0:
				factors.append(i)
				n = n/i
				break
			i+=1
	return factors

count = raw_input("Input maximum value:  ")
count = int(count)

for j in xrange(2, count+1):
		
	marsenne = math.log(j+1, 2) == int(math.log(j+1, 2))
	if marsenne:
		currentfactors = primefactor(j)
		if len(currentfactors) == 1:
			print "This one's prime:  ", j