
import math
fib = [0, 1]

while math.log(fib[-1], 10) < 999:
	fib.append(fib[-1] + fib[-2])

print fib[-1]
print len(fib) - 1