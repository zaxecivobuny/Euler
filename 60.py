from useful import checkprime, get_primes

prime_list = []
test_group = []

def is_prime(n):
    return checkprime(n)

# takes two ints, tries concatenating them in both permutations
# if either concat is composite, returns false
# otherwise, both are prime, and returns true
def check_concats_for_prime(a,b):
    return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))


# takes a list of ints, recursively checks pairs for primality
def check_primeness_by_concatenation(numlist):

    if len(numlist) == 2:
        return check_concats_for_prime(numlist[0],numlist[1])
    elif len(numlist) > 2:
        for number in numlist[1:]:
            if not check_concats_for_prime(numlist[0], number):
                return False
        if not check_primeness_by_concatenation(numlist[1:]):
            return False


    return True

# for i in get_primes(10000):
#     print i 
#     prime_list.append(i)

# print prime_list
# print len(prime_list)

# iterates the list of primes to the next version
# check the last prime in master_list that is present in primelist
# if all primes lower than that have been tried, then
def iterate_primes_in_list(primelist):
    global master_list
    master_list_index_of_top = master_list.index(primelist[-1])
    primesetlength = master_list_index_of_top + 1
    spaces = primesetlength - len(primelist)
    master_list_index_of_bottom = master_list.index(primelist[0])
    if master_list[spaces] == primelist[0]:
        #print "INCREMENTING", primelist
        primelist = master_list[:len(primelist)-1]
        #print master_list_index_of_top
        primelist.append(master_list[master_list_index_of_top+1])
        #print primelist
        return primelist
    else:
        lastprime = master_list_index_of_bottom
        for prime in master_list[master_list_index_of_bottom:]:
            #print "prime is", prime
            if not prime in primelist:
                primelist[primelist.index(lastprime)] = prime
                return primelist
            else:
                lastprime = prime



listlength = 4
master_list = []
for i in get_primes(10000):
    #print i 
    master_list.append(i)
seedlist = master_list[:listlength]
print seedlist

a = [3,7,109,673]
workinglist = seedlist[:]
for i in xrange(100000):
    #print "workinglist: ", workinglist
    if workinglist[-1] == 673:
        print workinglist
    if workinglist == a:
        print "should succeed"
        break
    if check_primeness_by_concatenation(workinglist):
        print "SUCCESS"
        break
    else:
        workinglist = iterate_primes_in_list(workinglist)

print workinglist

