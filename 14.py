
def collatzlib(n):
	t = n
	c = {}
	l = []
	count = 1
	while not t in c:
		l.append(t)
		if (t % 2) == 0:
			t = t / 2
		else:
			t = (3 * t) + 1
		count += 1

def collatzall(n):
	c = []
	while  n > 1:
		if (n % 2) == 0:
			n = n / 2
		else:
			n = (3 * n) + 1
		c.append(n)
	return c

def collatz(m, l):
	n = m
	c = 0
	while n > 1:
		if (n % 2) == 0:
			n = n / 2
		else:
			n = (3 * n) + 1
		c += 1
		if n in l:
			l[m] = l[n] + c
			break
	if not m in l:
		l[m] = c
	return l

longest  = [1,0]
d = {1:1}

for i in range(1, 1000 * 1000):
	m = collatz(i, d)
	longest[1] = max(longest[1], m[i])
	if longest[1] == m[i]:
		longest[0] = i


print longest