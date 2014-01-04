
import math

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
iterations = 1000 * 1000
iterations -= 1
result = []

for i in range(len(l)):
	n = int( iterations / math.factorial( len(l) - 1 ) )
	result.append(l.pop(n))
	iterations = iterations % math.factorial( len(l) )

print result