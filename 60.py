from useful import checkprime, get_primes

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

# takes a list of ints, returns false (TRUE?) if any pair inside is already in the fail list
def check_if_primes_already_failed(working_list):
    print "go"


# this function iterates the working list of primes to the next smallest group of size N 
# first, it finds the lowest prime in the working list. call that A
# second, it finds the lowest prime in the master list that is not in the working list. call that B
# if the space between the two in master is one, we replace A with B
# if the space is greater than two, we find the highest prime in working list that is less than B, call that C
#   then we replace C with B, and backfill all lower positions in working list with the smallest primes in order until working list is filled up to the location of C
def alt_iterate_primes_in_list(working_list):
    global master_list
    lowest_prime_index_in_master = master_list.index(working_list[0])    
    for i in xrange(1,len(working_list)+1):
        if not master_list[lowest_prime_index_in_master + i] in working_list:
            next_largest_index_in_master = lowest_prime_index_in_master + i
            break
    i -= 1
    if i == 1:
        working_list[i] = master_list[next_largest_index_in_master]
    else:
        working_list[i] = master_list[next_largest_index_in_master]
        remaining_space = len(working_list) - i
        working_list[:i] = master_list[:i]

    return working_list

listlength = 5
master_list = []
for i in get_primes(10000):
    master_list.append(i)

master_list.remove(2)
master_list.remove(5)
seedlist = master_list[:listlength]
print seedlist
a = [3,7,109,673]
workinglist = seedlist[:]

# cheatyface
index = master_list.index(a[listlength-2])
workinglist = a[:listlength-1]
workinglist.append(master_list[index+1])
# /cheatyface

print workinglist

while True:
    if check_primeness_by_concatenation(workinglist):
        print "SUCCESS"
        break
    else:
        # workinglist = alt_iterate_primes_in_list(workinglist)
        index += 1
        workinglist[-1] = master_list[index]


print workinglist
print sum(workinglist)


# SUCCESS
# [3, 7, 109, 673]
# [Finished in 136.8s]

# same answer in 118 seconds without 2 or 5 in the list


# b = set({1,2})
# c = set({3,4})

# print c

# ran on 5 for 24 hours, no result.