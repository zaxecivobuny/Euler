import math

def checkpalindrome(number):
    digits = str(number)
    i = 0
    while i < len(digits)/2:
        if not (digits[i] == digits[-1*(i+1)]):
            return False
        i+=1
    return True

palindrome = False
while not palindrome:
    i = 999    
    while i > 99:
        j = 999
        while j > 99:
            product = i * j
            palindrome = checkpalindrome(product)
            if palindrome:
                print product
                print i
                print j
                break
            j -= 1
        if palindrome:
            break
        #print i, j
        i -= 1
        