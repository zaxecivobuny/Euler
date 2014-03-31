def get_primes(max_number):
    global known_composites
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

def checkprime(n):
    a = 0.0
    a = n ** .5
    if n < 2:
        return False
    for i in get_primes(int(a) + 1):
        if n % i == 0:
            return False
    return True

def add_diagonals(layer):
    global count
    global diagonals
    count += 2
    for i in xrange(4):
        diagonals.append(diagonals[-1] + count)
    return diagonals

def make_diagonals(layers):
    global count
    count = 0
    global diagonals
    diagonals = [1]
    for i in xrange(1,layers):
        count += 2
        for j in xrange(0,4):
            diagonals.append(diagonals[-1] + count)
    return diagonals

def prime_ratio(array):
    global primecount
    localarray = []
    for i in xrange(4):
        localarray.append(array[i-4])

    for i in localarray:
        if checkprime(i):
            primecount +=1
    print "primecount", primecount
    return (primecount + 0.0) / len(array)

primecount = 0
layer = 4
alldiagonals = make_diagonals(1)
for i in xrange(3):
    
    alldiagonals = add_diagonals(1)

print alldiagonals
current_ratio = prime_ratio(alldiagonals)
print current_ratio
while (current_ratio > .80):
    layer+=1
    current_ratio = prime_ratio(add_diagonals(layer))
    if (layer%100 == 0):
        print layer
        print current_ratio

print current_ratio
sidelength = (2 * layer) - 1
print layer, sidelength
layer-=1
sidelength = (2 * layer) - 1

print layer, sidelength


#layer = (sidelength + 1) / 2