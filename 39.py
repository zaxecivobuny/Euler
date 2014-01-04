#takes 20 minutes


def checkright(*args):
	l = []
	for i in args:
		l.append(i)
	l.sort()
	if not len(l) == 3:
		return False
	return ((l[0] * l[0]) + (l[1] * l[1]) == l[2] * l[2])


maxperimeter = 1000
maxtri = []
triangles = []
maxlen = 0
biggest = 0


for t in xrange(3,maxperimeter + 1):
	perimeter = t
	triangles = []
	for i in xrange(1,perimeter/2):
		for j in xrange(i, perimeter-i):
			k = perimeter - i - j
			if checkright(i,j,k):
				temp = [i,j,k]
				temp.sort()
				if triangles == []:
					triangles.append(temp)
				else:
					y = True
					for m in triangles:
						if m == temp:
							y = False
					if y:
						triangles.append(temp)

	if len(triangles) > maxlen:
		maxlen = len(triangles)
		maxtri = triangles
		biggest = t


print maxtri
print biggest
