def reverseandadd(n):
    stringn = str(n)
    flipnum = int(stringn[::-1])
    return n + flipnum

def isPalindrome(n):
    stringn = str(n)
    if stringn == stringn[::-1]:
        return True
    return False

def checklychrel(n):
    iterations = 1
    i = n
    i = reverseandadd(i)
    while iterations < 50 and not isPalindrome(i):
        i = reverseandadd(i)
        iterations += 1
    if iterations < 50:
        return False
    return True

lychrels = []

for i in xrange(1,10000):
    if checklychrel(i):
        lychrels.append(i)
print len(lychrels)
print lychrels