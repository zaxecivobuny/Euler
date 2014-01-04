def factorial(n):
	if n < 2:
		return 1
	fact = 1
	for i in xrange(2, n + 1 ):
		fact *= i
	return fact

def sumdigitfacts(n):
	digits = []
	facts = []
	a = str(n)
	for i in a:
		digits.append(int(i))
		facts.append( factorial( digits[-1] ) )
	return sum(facts)

listem = []
for i in range(10, 50000):
	if i == sumdigitfacts(i):
		listem.append(i)

print listem
print sum(listem)