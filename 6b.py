def checkpalindrome(number):
    digits = str(number)
    i = 0
    while i < len(digits)/2:
        if not (digits[i] == digits[-1*(i+1)]):
            return False
        i+=1
    return True
    
def primefactor(n):
	factors = []
	while n>1:
		i=2
		while i<=n:
			if n%i == 0:
				factors.append(i)
				n = n/i
				break
			i+=1
	return factors

max = (999**2) + 1
min = 99 * 99

while max > min:
    max -= 2
    if checkpalindrome(max):
        maxfactors = primefactor(max)
        print primefactor(max)
        if len(maxfactors) == 2:
            if len(str(maxfactors[-1])) == 3 and len(str(maxfactors[-2])) == 3:
                print max
                break
    

    
print maxfactors

