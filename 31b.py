def counttheways(l, total):
	ways = 0
	if len(l) == 0:
		print 0
		return 0
		
	current = l.pop()
	if current == total:
		print current
		ways += 1
		ways += counttheways(l[:], total)
		return ways
		
	count = 1
	while current < total:
		total -= current
		ways += counttheways(l[:], total)
		count += 1
		print current
	print count
	return count


def countthewaysback(l, total):
	ways = 0
	if len(l) == 0:
		print 0
		return 0
		
	current = l.pop()
	if current == total:
		print current
		return 1
		
	count = 1
	while current < total:
		total -= current
		ways += counttheways(l[:], total)
		count += 1
		print current
	print count
	return count





if __name__ == "__main__":
	global grandtotal
	grandtotal = .05
	denominations = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
	denominations.reverse()
	print denominations
	ways = 0
	m = counttheways(denominations[:], grandtotal)
	for i in xrange(len(denominations)):
		ways += counttheways(denominations[:i], grandtotal)
	print ways
	print "M", m
