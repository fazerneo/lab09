class Fraction:
    def __init__(self, n, d):
        self.numerator = n
        if d==0:
            raise Exception("Denominator cannot be 0")
        else:
            self.denominator = d

    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)

    def __add__(self, other):
        f = Fraction(0,1)
        f.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        f.denominator = self.denominator * other.denominator
        return f

    def __sub__(self, other):
        f = Fraction(0,1)
        f.numerator = self.numerator * other.denominator - other.numerator * self.denominator
        f.denominator = self.denominator * other.denominator
        return f
    
    def __eq__(self, other):
        if self.numerator/self.denominator == other.numerator/other.denominator:
            return True
        else:
            return False

    def float(self):
        return self.numerator/self.denominator

    def __truediv__(self, other):
        ''' Dividing two fractions is the same as multiplying the first fraction by the reciprocal of the second fraction. '''
        divided_numerator = self.numerator * other.denominator
        divided_denominator = self.denominator * other.numerator
        return str(divided_numerator) + "/" + str(divided_denominator)        
        
    def invert(self):
        return str(self.denominator) + "/" + str(self.numerator)
    
f1 = Fraction(1, 3)
f2 = Fraction(3, 5)
f3 = Fraction(2, 6)
print(f1+f2)
print(f1-f2)
print(f1==f2)
print(f1==f3)

# tests
f4 = Fraction(2, 4)
f5 = Fraction(2, 10)
f6 = Fraction(7, 12)

# frac to float
print(f1.float())
print(f4.float())
print(f5.float())
print(f6.float())

# division
print(f1/f2)
print(f4/f5)
print(f4/f6)
print(f5/f6)

# invert
print(f2.invert())
print(f4.invert())
print(f5.invert())
print(f6.invert())
