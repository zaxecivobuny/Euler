
most = 0

for denom in range(2, 11):
	decimal = 1.0/denom
	decimal *= 1000
	decimal -= int(decimal)
	repeater = False
	count = 1
	while not repeater:
		compar = int( decimal * (10 ** ( count + 1 ) ) )
		compar = str(compar)
		for j in xrange(len(compar))
			if compar
