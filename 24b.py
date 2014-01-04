
import math
def iterate(l):
	for i in range(len(l)):
		n = len(l) - i -1
		if l[n] > l[n - 1]:
			tempfront = l[:n-1]
			tempback = l[n-1:]
			holder = tempback[0]
			tempback.sort()
			for j in xrange(len(tempback)):
				if tempback[j] > holder:
					tempfront.append(tempback.pop(j))
					break
			return tempfront + tempback
	return l	

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(1, 1000 * 1000):
	#print "list", list
	list = iterate(list)
	#if i % math.factorial(9) == 0:
	#	print list

print list