
def gettri(n):
	return (n * (n + 1)) / 2

def ispenta(n):
	a = 0.0
	a = ((((24 * n) + 1) ** .5) + 1) / 6
	return a == int(a)

def ishexa(n):
	a = 0.0
	a = ((((8 * n) + 1) ** .5) + 1) / 4
	return a == int(a)

n = 286

while True:
	t = gettri(n)
	if ispenta(t) and ishexa(t):
		print t
		print n
		break
	else:
		n += 1