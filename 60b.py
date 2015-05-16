# recursive pair set creation. dis gon be good.

from useful import checkprime, get_primes

def is_prime(n):
    return checkprime(n)

# takes two ints, tries concatenating them in both permutations
# if either concat is composite, returns false
# otherwise, both are prime, and returns true
def check_concats_for_prime(a,b):
    return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))

# takes a prime for pairing, and a set of primes
# loops through the set, building a new set of primes that concat with the initial prime both ways to make a new prime
def get_prime_subset(pairing_prime, prime_set):
    global listlength
    global depth
    depth += 1
    if len(prime_set) == 0 or depth > listlength:
        print [pairing_prime]
        return [pairing_prime]
    prime_subset = []
    for prime_from_set in prime_set:
        if check_concats_for_prime(pairing_prime, prime_from_set):
            prime_subset.append(prime_from_set)

    prime_list_of_lists = []
    for i,p in enumerate(prime_subset):
        for j in get_prime_subset(p,prime_subset):
                prime_list_of_lists.append([[pairing_prime] + j])

    # for index, prime_from_subset in enumerate(prime_subset):
    #     get_prime_subset(pairing_prime_list + [prime_from_subset], prime_subset[index:])
    print "prime_list_of_lists", prime_list_of_lists
    return prime_list_of_lists



# start by setting listlength to n and getting an initial list of primes under 10,000 to draw on for later

listlength = 4
depth = 0
list_of_lists = []
master_list = []
for i in get_primes(10000):
    master_list.append(i)

# 2 and 5 are the only primes that end in 2 or 5
# we remove them from our list of primes
master_list.remove(2)
master_list.remove(5)

# seedlist will be the subset of the master list that our workinglist draws from. It's max will increment in every greater cycle    
seedlist = master_list[:listlength]

print len(master_list)

testpass = get_prime_subset(3,master_list[1:])
print len(testpass)

print testpass

test_list = []
for i in xrange(listlength):
    currentprime = 3


while True:
    test_list = [3]
    break


