
most = 0
mostindex = 1

for denom in xrange(3, 11, 2):
	frac = 1.0/denom
	print denom, " ",  frac
	count = 1
	while True:
		nines = (10 ** count) - 1
		print count
		if frac * nines == int(frac*nines):
			break
		count += 1
	most = max(most, count)
	if most == count:
		mostindex = denom
print most
print mostindex