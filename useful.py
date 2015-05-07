def get_primes(max_number):
	known_composites = {}
	i = 2
	while i < max_number:
		if not i in known_composites:
			yield i
			known_composites[i*i] = [i]
		else:
			for j in known_composites[i]:
				known_composites.setdefault(i + j, []).append(j)
			del known_composites[i]
		i += 1

def checkprime(n):
	a = 0.0
	a = n ** .5
	if n < 2:
		return False
	for i in get_primes(int(a) + 1):
		if n % i == 0:
			return False
	return True

def digitize(n):
	a = str(n)
	b = []
	for i in a:
		b.append(int(i))
	return b

def undigitize(l):
	temp = l[:]
	n = temp.pop()
	place = 10
	while len(temp) >= 1:
		n += (temp.pop() * place)
		place *= 10
	return n

def factorial(n):
	if n < 2:
		return 1
	p = n
	while n > 1:
		n -= 1
		p *= n
	return p


class Fraction:
    def __init__(self, numerator = 1, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator
    def invert (self):
        temp = self.numerator
        self.numerator = self.denominator
        self.denominator = temp
        return self

    def __repr__(self):
        p = str(self.numerator)
        p += "/"
        p += str(self.denominator)
        return p

    def __add__(self,a):
        if self.denominator == a.denominator:
            return Fraction(self.numerator+a.numerator,self.denominator)
        else:
            temp = a.denominator
            num1 = a.numerator * self.denominator
            denom = a.denominator * self.denominator
            num2 = self.numerator * temp
            return Fraction(num1+num2,denom)
    
    def __mul__(self,a):
        return Fraction(self.numerator*a.numerator,self.denominator*a.denominator)

    def __div__(self,a):
        temp = a.invert()
        return self * temp

    def __sub__(self, a):
        temp = Fraction(a.numerator * -1, a.denominator)
        return self + temp

    def reduce(self):
        num = self.numerator
        denom = self.denominator
        if (num == 1 or denom == 1):
            return Fraction(num,denom)
        for i in get_primes( min(num,denom) + 1 ):
            while ((num % i == 0) and (denom % i == 0)):
                num /= i
                denom /= i
        self.numerator = num
        self.denominator = denom
        return self