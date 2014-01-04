
def checkpent(n):
	global pentagonals
	global count
	while pentagonals[-1] < n:
		count += 1
		pentagonals.append(pentagonals[-1] + (3 * (count - 1) + 1) )
	for i in pentagonals:
		if n == i:
			return True
	return False



def maing():
	global pentagonals
	pentagonals = [1]
	global count
	count = 1
	biglist = []
	checkpent(5000)
	print pentagonals
	for j in xrange(1,20):
		for i in xrange(len(pentagonals)):
			a = pentagonals[i]
			b = pentagonals[i+j]
			if checkpent(a+b) and checkpent(b-a):
				biglist.append(a)
				biglist.append(b)

	print biglist
	print biglist[1]-biglist[0]
maing()