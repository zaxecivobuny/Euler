from useful import checkprime, get_primes

def slowTest(n):
    for i in get_primes( int(n**.5)+1 ):
        if n%i == 0:
            return False

    return True
def isPrime(n):
    global primesList
    if n in primesList:
        return True
    elif n < primesList[-1]:
        return False
    elif (n**.5) > primesList[-1]:
        return slowTest(n)
    elif (n**.5) == primesList[-1]:
        return False
    else:
        for i in primesList:
            if i > n**.5:
                return True
            elif n%i==0:
                return False

def get_answer():
    global primesList
    smallestSum = 99999999

    def check_concats_for_prime(a,b):
        return isPrime(int(str(a) + str(b))) and isPrime(int(str(b) + str(a)))

    maxPrime = 10000
    primesList = []
    smallestSet = [99999999,0,0,0]

    for i in get_primes(maxPrime):
        primesList.append(i)

    primesList.remove(2)
    primesList.remove(5)

    for index0,i in enumerate(primesList):
        for index1,j in enumerate(primesList[index0+1:]):
            if not check_concats_for_prime(i,j):
                continue
            for index2,k in enumerate(primesList[index1+1:]):
                if not (check_concats_for_prime(i,k) and check_concats_for_prime(j,k)):
                    continue
                for index3,l in enumerate(primesList[index2+1:]):
                    if not (check_concats_for_prime(i,l) and check_concats_for_prime(j,l) and check_concats_for_prime(k,l)):
                        continue
                    for index4, m in enumerate(primesList[index3+1:]):
                        if (check_concats_for_prime(m,i) and check_concats_for_prime(m,j) and check_concats_for_prime(m,k) and check_concats_for_prime(m,l)):
                            if i+j+k+l+m < smallestSum:
                                smallestSet = [i,j,k,l,m]
                                smallestSum = sum(smallestSet)
                                return smallestSet 

smallestSet = get_answer()
print smallestSet
print sum(smallestSet)
