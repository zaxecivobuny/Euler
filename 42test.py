
def wordscore(name):
	alphanum = 0
	for j in name:
		alphanum += (ord(j) - 64)
	return alphanum 

print wordscore("REMIND")