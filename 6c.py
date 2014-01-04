def checkpalindrome(number):
    digits = str(number)
    i = 0
    while i < len(digits)/2:
        if not (digits[i] == digits[-1*(i+1)]):
            return False
        i+=1
    return True
    
def trefactor(n):
    factorA = 999
    while factorA > 99:
        if n % factorA == 0:
            factorB = n/factorA
            if len(str(factorB)) == 3:
                return factorA
        factorA -= 1
    return 0

max = (999**2) + 1
min = 99 * 99

while max > min:
    max -= 1
    if checkpalindrome(max):
        largerfactor = trefactor(max)
        if not largerfactor == 0:
            print max
            print largerfactor
            print max/largerfactor
            break
    