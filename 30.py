
def sum_of_digits(n, x):
	digits = str(n)
	total = 0
	for i in digits:
		total += int(i) ** x
	if total == n:
		return True
	return False

l = []
for i in xrange(1000, 354294):
	if sum_of_digits(i, 5):
		l.append(i)

print l
print sum(l)

#[4150, 4151, 54748, 92727, 93084, 194979]
#443839