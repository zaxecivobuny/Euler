	


def counttheways0(l, total):
	print l
	print total
	ways = 0
	sublist = l[:]
	current = sublist.pop(0)
	if current > total:
		print 0
		print "ways", ways
		return ways
	else:
		for i in xrange(1, int((total / current))):
			n = i * current
			if n == total:
				ways += 1
				print "ways", ways
				return ways
			else:
				c = counttheways(sublist, total - n)
				print "sublist", sublist, "total", total, "total - n", total - n, "c=", c
				ways += c
	return ways



if __name__ == "__main__":
	denominations = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
	denominations.reverse()
	print denominations
	m = counttheways(denominations, .05)

	print "M", m
