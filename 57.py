from useful import get_primes

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

def cont_frac(iter):
    total = Fraction(0)
    
    for i in xrange(iter):
        total = total + 2
        total.invert()

    total = total + 1
    return total

answer = 0
for i in xrange(1,1001):
    curr_frac = cont_frac(i)
    #print i, curr_frac, (len(str(curr_frac.numerator)) > len(str(curr_frac.denominator)))
    if (len(str(curr_frac.numerator)) > len(str(curr_frac.denominator))):
        answer += 1

print answer