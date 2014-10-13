#this Function takes an Integer as Argument and returns a List of prime factors

def primefactor(n):
	factors = []
	while n>1:
		for i in xrange (2, n+1):
			if n%i == 0:
				factors.append(i)
				n = n/i
				break
	return factors
	
#call = raw_input("> ")
#print primefactor(int(call))

key = 'aaz'
print key[:-1] + 'a'

a = "thesaurus"

if "the" in a:
    print a

print 0 + "a"