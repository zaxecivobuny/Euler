total = 50
count = 0

pence = 1
tupence = 2
shilling = 5
florin = 10
twentypee = 20
tenbob = 50
quid = 100
twopounds = 200

l = [0,0,0,0,0,0,0,0]
while l[0] <= total:
	l[1] = 0
	while l[1] <= total:
		l[2] = 0
		while l[2] <= total:
			l[3] = 0
			while l[3] <= total:
				l[4] = 0
				while l[4] <= total:
					l[5] = 0
					while l[5] <= total:
						l[6] = 0
						while l[6] <= total:
							l[7] = 0
							while l[7] <= total:
								if sum(l) == total:
									count += 1
								l[7] += twopounds
							
							if sum(l) == total:
								count += 1
							l[6] += quid
						
						if sum(l) == total:
							count += 1
						l[5] += tenbob
					
					if sum(l) == total:
						count += 1
					l[4] += twentypee
				if sum(l) == total:
					count += 1
				l[3] += florin
			if sum(l) == total:
				count += 1
			l[2] += shilling
		if sum(l) == total:
			count += 1
		l[1] += tupence
	if sum(l) == total:
		count += 1	
	l[0] += pence

print count