
def wordscore(name):
	alphanum = 0
	for j in name:
		alphanum += (ord(j) - 64)
	return alphanum 

def checktriangle(n):
	global count
	global trinums
	global lasttri
	while lasttri < n:
		lasttri += count
		trinums[lasttri] = count
		count += 1
	return n in trinums

count = 1
lasttri = 0
trinums = {}
total = 0


f = open('c:\\LPTHW\\euler\\words.txt')
text = f.read()
words = text.split(',')
for i in words:
	if checktriangle(wordscore(i[1:-1])):
		#print i[1:-1]
		#print wordscore(i[1:-1])
		total += 1

print total


