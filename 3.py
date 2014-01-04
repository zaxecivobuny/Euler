sumsq = 0
upper = 100

for i in range(1, upper + 1):
	sumsq += (i*i)

sqsum = ((upper*upper)+upper)/2
sqsum *= sqsum

print abs(sqsum-sumsq)
