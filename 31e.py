
def counttheways(l, total):
	global count
	current = l.pop()
	if current == 1:
		count += 1
		return True
	if current > total:
		counttheways(l[:], total)
	if current == total:
		count += 1
		counttheways(l[:], total)
	if current < total:
		most = total / current
		while most >= 0:
			subtotal = total - (most * current)
			counttheways(l[:], subtotal)
			most -= 1

count = 0
l = [0,0,0,0,0,0,0,0]
denoms = [1,2,5,10,20,50,100,200]

counttheways(denoms[:], 200)
print count