
import math

def getd(n):
	return (3 * (n - 1)) + 1

def getp(n):
	return (n * ((3 * n) - 1)) / 2

# d = 3(n-1) + 1
def pentdiff(d):
	return d + 3

def checkd(a):
	temp = a + 0.0
	temp -= 1
	temp /= 3
	temp += 1
	return temp == int(temp)

def checkp(a):
	if a < 1:
		return False
	temp = a + 0.0
	b = math.sqrt((24 * temp) + 1)
	if not b == int(b):
		return False
	n = (1 - b) / 6
	m = (b + 1) / 6
	return m == int(m) or n == int(n)

thepair = []
bestpair = [1820,2262]
print checkp(275)
for j in xrange(1, 10000):
	for i in xrange(1, 30 * 1000):
		a = getp(i)
		b = getp(j + i)
		if (b-a) > 3000:
			break
		if checkp(b - a):
			if checkp(a + b):
				thepair.append(i)
				thepair.append(j)
				thepair.append(getp(i))
				thepair.append(getp(i+j))
				if b - a < bestpair[-1] - bestpair[-2]:
					bestpair[0] = a
					bestpair[1] = b

print thepair

print bestpair
print bestpair[-1] - bestpair[-2]

# 1820, 2262, 442