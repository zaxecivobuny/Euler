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

for j in range(2, 11):
	print j
	factors = primefactor(j)
	print factors
	tempbig = bigfactors[:]
	while len(tempbig) > 0 and len(factors) > 0:
		print "bigfactors at start of loop: ",bigfactors
		if factors[-1] == tempbig[-1]:
			factors.pop()
			tempbig.pop()
			print "after a pop1", bigfactors
		elif factors[-1] < tempbig[-1]:
			tempbig.pop()
			print "after a pop2", bigfactors
		else:
			print "before a pop", bigfactors
			bigfactors.append(factors.pop())
			print "ADDING"
			print bigfactors
	bigfactors.sort()

print bigfactors
product = 1
for i in bigfactors:
	product *= i

print product
	
	
			
			