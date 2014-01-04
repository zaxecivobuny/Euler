
n = 1

while n > 0:
	codds = 0.0
	cval = 0.0
	for i in range(n):
		odds = 0.0
		odds = ((35.0 ** (i)) / (36.0 ** (i + 1)))
		if n > 1:
			people = 9 * (10 ** (i - 1))
		else:
			people = 1
		codds += odds
		cval = odds * people

	print codds
	print cval
	n = raw_input("How many?")
	n = int(n)