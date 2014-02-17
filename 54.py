
# U R2 F B R B2 R U2 L B2 R U' D' R2 F R' L B2 U2 F2

def intify(s):
	
	# converts face cards to number values
	
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
	
	# sorts the hand by card value, lowest first
	
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
#	print temphand
	return temphand[:]

def countplaces(A):
#	print "A at start of countplaces", A
	# returns a count of how many 2s, 3s, etc. (useful for determining pairs, full house, etc)

	places = []
	for i in xrange(15):
		places.append(0)
	for i in xrange(5):
#		print "A", A
#		print "i", i

		places[intify(A[i][0])] += 1
	return places

def highesttwopair(A,B):

	# compares two hands with two pair, returns 1 if first hand wins, 0 if second does.

	Aplaces = countplaces(A)
	Bplaces = countplaces(B)
	for i in range(len(Aplaces) - 1 ,0,-1):
		if Aplaces[i] == 2 and not Bplaces[i] == 2:
			return 1
		if Bplaces[i] == 2 and not Aplaces[i] == 2:
			return 0
	return highcardshowdown(A,B)

def highestofakind(A,B,n):
	Aplaces = countplaces(A)
	Bplaces = countplaces(B)
	for i in range(len(Aplaces)):
		if Aplaces[i] == n:
			Akind = i
		if Bplaces[i] == n:
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

def highcardshowdown(A,B):
#	print "A at start of highcardshowdown", A
	Aplaces = countplaces(A)
	Bplaces = countplaces(B)
	for i in range(len(Aplaces)-1,0,-1):
		if Aplaces[i] == 1 and not Bplaces[i] == 1:
			return 1
		if Bplaces[i] == 1 and not Aplaces[i] == 1:
			return 0
	return 0

def break_tie(A,B,rank):
#	print "A at start of break_tie", A
	if rank in (8, 5, 4, 0):
		return highcardshowdown(A,B)
	if rank in (6, 3):
		m = highestofakind(A,B,3)
		if not m == -1:
			return m
		else:
			return highcardshowdown(A,B)
	if rank == 7:
		#highest foak
		m = highestofakind(A,B,4)
		if not m == -1:
			return m
		else:
			return highcardshowdown(A,B)
	if rank == 2:
		#highest two pairs
		return highesttwopair(A,B)
	if rank in (1, 6):
		#highest pair
		m = highestofakind(A,B,2)
		print m
		if not m == -1:
			return m
		else:
			return highcardshowdown(A,B)
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
#	print "A at start of rank_hand", A
	rank = 0
	places = countplaces(A)
	places.sort()
	A = sort_hand(A)
#	print "A after sort_hand", A
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
#		print "A before rank_hand ends", A
		return 0

def compare_hands(A,B):
	#print "A at start of compare_hands", A
	x = rank_hand(A[:])
	y = rank_hand(B[:])
	print x,y
#	print "A after rank_hand", A
#	print "B after rank_hand", B
	if x == y:
		return break_tie(A, B, x)
	if x > y:
		return 1
	return 0


def main():
	score = 0
	f = open('poker.txt')
	count = 1
	for line in f:
		line = line[0:-1]
		hands = line[0:].split(" ")
		A = hands[0:5]
		B = hands[5:10]
#		print "before the comparison, A and B are ", A, B
		print "count", count, compare_hands(A[:], B[:])
		score += compare_hands(A[:], B[:])
		count += 1

	f.close()
	print score

main()