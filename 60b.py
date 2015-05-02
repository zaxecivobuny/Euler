# IGNORE ME!

from useful import checkprime, get_primes


# start by setting listlength to n and getting an initial list of primes under 10,000 to draw on for later

listlength = 4
master_list = []
for i in get_primes(10000):
    master_list.append(i)

# seedlist will be the subset of the master list that our workinglist draws from. It's max will increment in every greater cycle    
seedlist = master_list[:listlength]

print len(master_list)