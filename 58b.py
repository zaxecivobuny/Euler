import math
from useful import checkprime
# rather than generating an actual spiral,
# we can generate a list of the diagonal numbers
# here's how:
# each layer has four corners (which comprise the diagonals)
# the values of these corners are the same distance apart (sidelength - 1)
# the first sidelength is one
# the next is three
# the next is five
# note that the sidelength is the same as the square root of the bottom right corner of the layer

# function that takes two arguments
# the first is an array,
# the second is the number of layers to add to the array
def add_layers(array = [1], new_layers = 0):
    side_length = int(math.sqrt(array[-1]))
    delta = side_length - 1

    for i in xrange(new_layers):
        delta += 2
        for j in xrange(4):
            array.append(array[-1] + delta)

    return array

def check_diagonals(array, layers_to_check = 1):
    array_to_check = []
    diagonals_to_check = layers_to_check * 4
    for i in xrange(diagonals_to_check):
        array_to_check.append(array[i - diagonals_to_check])

    return array_to_check

def count_diagonal_primes(array):
    count = 0
    for i in array:
        if checkprime(i):
            count += 1
    return count

diagonals_array = [1]
diagonals_array = add_layers(diagonals_array, 3)
totalprimes = count_diagonal_primes(check_diagonals(diagonals_array,3))
prime_ratio = (totalprimes + 0.0) / len(diagonals_array)
count = 4
print totalprimes
print diagonals_array

while True:
    count += 1
    diagonals_array = add_layers(diagonals_array,1)
    #print diagonals_array
    totalprimes += count_diagonal_primes(check_diagonals(diagonals_array,1))
    prime_ratio = (totalprimes + 0.0) / len(diagonals_array)
    if prime_ratio < .1:
        break
    if count % 1000 == 0:
        print count
        print prime_ratio


print prime_ratio

side_length = int(math.sqrt( diagonals_array[-1] ))

print side_length