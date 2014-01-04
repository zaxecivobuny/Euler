fib = [1,1]
sum = 0
count = 2
while fib[-1] < 4000000:
	fib.append(fib[-1] + fib[-2])
	if fib[count]%2 == 0 and fib[-1]<4000000:
		sum+=fib[count]
	count+=1
	
print sum