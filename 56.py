
def digitsum(n):
    stringn = str(n)
    sumdigits = 0
    for i in stringn:
        sumdigits += int(i)
    return sumdigits


maximum = 0
save = 0
saveB = 0

for i in xrange(0,100):
    for j in xrange(0,100):

        power = i ** (j)
        if digitsum(power) > maximum:
            maximum = digitsum(power)
            save = i
            saveB = j

print maximum, save, saveB

