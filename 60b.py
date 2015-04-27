# IGNORE ME!

from useful import checkprime, get_primes

# start with a set of n primes, where n is 4 in the problem example
# check all iterations of that prime set in ascending sum order
# if found, return the set
# otherwise, increase the set size by one prime and repeat this and the last two steps


# start by setting listlength to n and getting an initial set of 10,000 primes to draw on for later

listlength = 4
master_list = []
for i in get_primes(10000):
    master_list.append(i)

# seedlist will be the subset of the master list that our workinglist draws from. It's max will increment in every greater cycle    
seedlist = master_list[:listlength]

