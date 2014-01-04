def numbertoletters(n):
	l = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13: 'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
	letters = ''
	if n > 999:
		letters = l[n / 1000] + "thousand"
		n = n % 1000
		if n == 0:
			return letters
		#else:
		#	letters += "and"
	if n >99:
		letters += l[n / 100] + "hundred"
		n = n % 100
		if n == 0:
			return letters
		else:
			letters += "and"
	if n < 20:
		letters += l[n]
	elif n % 10 == 0:
		letters += l[n]
	else:
		letters += l[n - (n % 10)] + l[n % 10]


	return letters

total = 0

print numbertoletters(2000)

for i in range (1, 1001):
	 total += len(numbertoletters(i))

print total
