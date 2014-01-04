
# U R2 F B R B2 R U2 L B2 R U' D' R2 F R' L B2 U2 F2

def intify(s):
	if s == "A":
		return 14
	elif s == "K":
		return 13
	elif s == "Q":
		return 12
	elif s == "J":
		return 11
	elif s == "T":
		return 10
	else:
		return int(s)

def sort_hand(A):
	temphand = []
	while len(temphand) < 5:
		least = 100
		index = 0
		for i in xrange(len(A)):
			cardnumber = intify(A[i][0])
			if cardnumber < least:
				index = i
				least = cardnumber
		temphand.append(A.pop(index))
	return temphand

def countplaces(A):
	places = []
	for i in xrange(15):
		places.append(0)
	for i in xrange(5):
		places[intify(A[i][0])] += 1
	return places

def highesttwopair(A,B):
	Aplaces = countplaces(A)
	Bplaces = countplaces(B)
	for i in range(len(Aplaces) - 1 ,0,-1):
		if Aplaces[i] == 2 and not Bplaces[i] == 2:
			return 1
		if Bplaces[i] == 2 and not Aplaces[i] == 2:
			return 0
	if highcard(A)>highcard(B):
		return 1

def highestofakind(A,B,n):
	Aplaces = countplaces(A)
	Bplaces = countplaces(B)
	for i in range(len(places)):
		if Aplaces[i] == n:
			Akind = i
		if Bplaces[i] == n
			Bkind = i
	if Akind > Bkind:
		return 1
	elif Akind == Bkind:
		return -1
	else:
		return 0

def highcard(A):
	places = countplaces(A)
	return intify(A[-1][0])

def break_tie(A,B,rank):
	if rank in (8, 5, 4, 0):
		if highcard(A) > highcard(B):
			return 1
	if rank in (6, 3):
		if highestofakind(A,3)>highestofakind(B,3):
			return 1
	if rank == 7:
		#highest foak
		m = highestofakind(A,B,4)
		if not m == -1:
				
	if rank == 2:
		#highest two pairs
		return highesttwopair(A,B)
	if rank == 1:
		#highest pair
		if highestofakind(A,2)>highestofakind(B,2):
			return 1
	return 0


def pair(A, places):
	return places[-1] == 2

def twopair(A, places):
	return places[-1] == 2 and places[-2] == 2

def threeofakind(A, places):
	return places[-1] == 3

def straight(A):
	for i in xrange(4):
		if not intify(A[i][0]) + 1 == intify(A[i+1][0]):
			return False
	return True

def flush(A):
	for i in xrange(4):
		if not A[i][1] == A[i+1][1]:
			return False
	return True

def fullhouse(A, places):
	return places[-1] == 3 and places[-2] == 2

def foak(A, places):
	return places[-1] == 4

def straightflush(A):
	return straight(A) and flush(A)

def rank_hand(A):
	rank = 0
	places = countplaces(A)
	places.sort()
	# high card = 0
	# pair = 1
	# two pair = 2
	# three of a kind = 3
	# straight = 4
	# flush = 5
	# full house = 6
	# four of a kind = 7
	# straight flush = 8
	if flush(A) and straight(A):
		return 8
	elif foak(A, places):
		return 7
	elif fullhouse(A, places):
		return 6
	elif flush(A):
		return 5
	elif straight(A):
		return 4
	elif threeofakind(A, places):
		return 3
	elif twopair(A, places):
		return 2
	elif pair(A, places):
		return 1
	else:
		return 0

def compare_hands(A,B):
	x = rank_hand(A)
	y = rank_hand(B)
	#print x, y
	if x == y:
		return break_tie(A, B, x)
	if x > y:
		return 1
	return 0


score = 0
f = open('c:\\LPTHW\\euler\\pokertest.txt')
for line in f:
	hands = line[0:-1].split(" ")
	A = hands[0:5]
	B = hands[5:10]
	#print A
	#print B
	print compare_hands(A,B)
	score += compare_hands(A, B)

print score