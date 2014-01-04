n = 21
found = False

while not found:
	works = True
	for i in range(1, 21):
		if not n%i == 0:
			works = False
	if works:
		found = True
	else:
		n+=1
	if n%10000 == 0:
		print n
		
print n