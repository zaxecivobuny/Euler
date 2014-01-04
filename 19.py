months = [31,28,31,30,31,30,31,31,30,31,30,31]

day = 1
year = 1900
leapyear = False
for i in months:
	day += i
	day %= 7

print day
year += 1
Sundays = 0

while year < 2001:
	if (year % 4 == 0) and not (year % 100 ==0 and not year % 400 == 0):
		leapyear = True
	else:
		leapyear = False
	for i in months:
		if day == 0:
			Sundays += 1
		day += i
		if i == 1 and leapyear:
			day+=1
		day %= 7
	year += 1

print Sundays