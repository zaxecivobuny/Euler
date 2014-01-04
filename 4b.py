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

bigfactors = [1]

#max = raw_input("Input max value: ")
#max = int(max)
max = 20

for j in xrange(2, max+1):
	factors = primefactor(j)
	tempbig = bigfactors[:]
	while len(tempbig) > 0 and len(factors) > 0:
		if factors[-1] == tempbig[-1]:
			factors.pop()
			tempbig.pop()
		elif factors[-1] < tempbig[-1]:
			tempbig.pop()
		else:
			bigfactors.append(factors.pop())
	bigfactors.sort()

print bigfactors
product = 1
for i in bigfactors:
	product *= i

print product
	
	
			
			