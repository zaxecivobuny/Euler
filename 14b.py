

c = {}


for i in range(1, 100):
	count = 1
	t = i
	while not t in c:
		c[t] = 0
		if (t % 2) == 0:
			t = t / 2
		else:
			t = (3 * t) + 1
		count += 1
	c[i] = count

