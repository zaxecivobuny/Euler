
def get_primes(max_number):
	known_composites = {}
	i = 2
	while i < max_number:
		if not i in known_composites:
			yield i
			known_composites[i*i] = [i]
		else:
			for j in known_composites[i]:
				known_composites.setdefault(i + j, []).append(j)
			del known_composites[i]
		i += 1

most = 1
primedict = {}
primelist = []
top = 1000 * 1000
first = 2

for i in get_primes(top):
	primedict[i] = 0
	primelist.append(i)

#print len(primelist)
#print primelist

for i in xrange(len(primelist)):     #run the loop for each prime in the list
	topindex = most + i
	total = sum(primelist[i:i + most + 1])
	if total > top:
		break
	else:
		while total <= top:
			#print i, total, count
			topindex += 1
			total += primelist[topindex]
		while not total in primedict:
			#print i, total, topindex
			total -= primelist[topindex]
			topindex -= 1
		topindex += 1
		if topindex - i > most:
			#print "topindex", topindex
			most = topindex - i
			first = primelist[i]
			firstindex = i
			biggest = total	
	

print ""
print most
#print first
#print primelist[firstindex:firstindex+most]
#print sum(primelist[firstindex:firstindex+most])
print biggest