from useful import get_primes, checkprime

def iterate_binary(b, l):
	# b is a string consisting of ones and zeros
	# returns an integer which is the next higher binary number
	# the returned number will be front-filled with zeros, such that it has length l
	temp = int(str(b),2)
	temp += 1
	return bin(temp)[2:].zfill(l)

def fill_spaces(b, n):
	# b is a string consisting of ones and zeros
	# n is an integer with length = (number of ones in b)
	# returns a string which replaces the ones in b with the digits of n
	stringed = str(n).zfill(get_spaces(b))
	spaced = ''
	count = 0
	for i in b:
		if i == '1':
			spaced += stringed[count]
			count += 1
		else:
			spaced += '0'
	return spaced

def get_spaces(b):
	# counts the number of ones in b
	count = 0
	for i in b:
		if i =='1':
			count += 1
	return count

def binary_compliment(b):
	# b is a string consisting of ones and zeros
	# returns an integer with the same length
	c = ''
	for i in b:
		if i == '1':
			c += '0'
		else:
			c += '1'
	return c	

def do_injection(n, b, i):
	# b is a string consisting of ones and zeros
	# n is the complement with filled spaces
	# i is a counter
	inject = i * int(b)
	result = n + inject


def count_primes_by_injection(n, b):
	global primes_to_find
	count = 0
	noncount = 0
	num = int(n)
	for i in xrange(10):
		inject = i * int(b)
		result = num + inject
		if checkprime(result) and result > int(b):
			#print 'result', result
			count += 1
		#else:
		#	noncount += 1
		#	if noncount > 10 - primes_to_find:
		#		return count

	return count

#print iterate_binary('1',1)


def maing():
	global primes_to_find
	length = 5
	spaces = 0
	primes_to_find = 8
	primes_found = 0

# 1s in binary are wildcard, 0s are iterating numbers 

	#print fill_spaces('0110','5')
	#print fill_spaces('11001', 563)
	#print binary_compliment('101011')
	#print count_primes_by_injection(56003, '00110')
	#print iterate_binary('0', 2)
	 
# start with a blank of length one in a number of length one. 
# Then inject the digits and count primes
# We check to see if the number of primes is enough. If so, stop.
# if not, we increase the length, and start iterating
# one iteration consists of trying every static combination of numbers and injecting integers
# in the next iteration, we shuffle the wildcards around and repeat the previous line, until the whole 

# repeat the following until you have the number of primes you seek
#	set binary to one
#	increase length by one
#	repeat the following until binary has a number of ones equal to it's length

	while primes_found < primes_to_find:
		binary = '0'
		#print binary
		length += 1
		binary = iterate_binary(binary, length)
		while len(binary) <= length:
			print "length", length, "binary", binary
			for static_number in xrange(1,10**get_spaces(binary_compliment(binary))):
				if binary[-1] == '1':
					break
				if binary[-1] == '0':
					while static_number % 2 == 0 or static_number % 5 == 0:
						static_number += 1

				#print "binary", binary
				static_string = str(static_number).zfill(length)
				fillednum = fill_spaces(binary_compliment(binary), static_number)
				#print "fillednum", fillednum
				primes_found = max(primes_found, count_primes_by_injection(fillednum, binary))
				if primes_found >= primes_to_find:
					print primes_found
					print binary, static_number
					return True
			binary = iterate_binary(binary, length)
			#if binary == "000010":
			#	print "done"
			#	return True
			#print "binary iteration"
			


maing()
#483 s without check


