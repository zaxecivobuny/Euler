import useful

prime_list = []
test_group = []

for i in useful.get_primes(10000):
    print i 
    prime_list.append(i)

print prime_list
print len(prime_list)