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

# this function iterates the working list of primes to the next smallest group of size N 
# first, it finds the lowest prime in the working list. call that A
# second, it finds the lowest prime in the master list that is not in the working list. call that B
# if the space between the two in master is one, we replace A with B
# if the space is greater than two, we find the highest prime in working list that is less than B, call that C
#   then we replace C with B, and backfill all lower positions in working list with the smallest primes in order until working list is filled up to the location of C

def alt_iterate_primes_in_list(working_list):
    print "let's do this"
    global master_list
    lowest_prime_index_in_master = master_list.index(working_list[0])
    
    for i in xrange(1,len(working_list)):
        if not master_list[lowest_prime_index_in_master + i] in working_list:
            next_largest_index_in_master = lowest_prime_index_in_master + i


# iterates the working list of primes to the next version
# there are three cases for this:
#   in the first, the four primes in the primelist are adjacent (no holes)
#       in this case, we increment the last position and start the remaining positions at the smallest list of primes to fill the space
#   in the second case, a hole exists
def iterate_primes_in_list(primelist,testflag):
    global master_list
    if testflag:
        print "primelist", primelist
    

    master_list_index_of_top = master_list.index(primelist[-1])
    primesetlength = master_list_index_of_top + 1
    spaces = primesetlength - len(primelist)
    master_list_index_of_bottom = master_list.index(primelist[0])
    
    if master_list[spaces] == primelist[0]:
        if testflag:
            print "INCREMENTING"
        primelist = master_list[:len(primelist)-1]
        #print master_list_index_of_top
        primelist.append(master_list[master_list_index_of_top+1])

        return primelist
    else:
        if not (2 in primelist :
            if testflag:
                print "reverse increment"
            for i in xrange(len(primelist)):
                # print i
                # print "primelist[-1 * (i + 1)]", primelist[-1 * (i + 1)]
                # print "master_list[master_list_index_of_top - i]", master_list[master_list_index_of_top - i]
                #print primelist
                #print "primelist[-1 * (i + 1)]", primelist[-1 * (i + 1)]  
                if not primelist[-1 * (i + 1)] == master_list[master_list_index_of_top - i]:
                    primelist[-1 * (i + 1)] = master_list[master_list_index_of_top - i]
                    primelist[:(len(primelist)-i-1)] = master_list[:(len(primelist)-i-1)]
                    return primelist

        lastprime = 2
        if testflag:
            print "forward increment"
        
            print "master_list", master_list[master_list_index_of_bottom:master_list_index_of_top]
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
for i in xrange(100):
    print "STEP =", i, "workinglist: ", workinglist
    if workinglist[-1] == 673:
        print workinglist

    #print workinglist
    if check_primeness_by_concatenation(workinglist):
        print "SUCCESS"
        break
    else:
        workinglist = iterate_primes_in_list(workinglist,False)

print workinglist

