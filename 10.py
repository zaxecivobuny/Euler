import math

primes = [2]
sum = 2
count = 3

while count < 2000000:
    composite = False
    primeindex = 0
    maxprime = math.sqrt(count)
    while primes[primeindex] <= maxprime:
        if count % primes[primeindex] == 0:
            composite = True
            break
        primeindex += 1
    if not composite:
        #print count
        sum += count
        primes.append(count)
    count +=2
    
print sum