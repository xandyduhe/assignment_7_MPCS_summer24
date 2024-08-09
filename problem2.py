# week 7 
# problem 2 

import math 



class Fraction:
    '''Attributes:
    numerator:
    denominator:
    '''

    def __init__(self, numerator, denominator):
        if not isinstance(denominator, int) or not isinstance(numerator, int):
            # did not pass 
            raise ValueError('Numerator and denominator must be integers')
        elif denominator == 0:
            # did not pass 
            raise ZeroDivisionError('Denominator cannot be zero.')
        
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()

    def _simplify(self):
        '''Simplify numberator and denominator using their GCD'''

        gcd = int(math.gcd(self.numerator, self.denominator))
        self.numerator //= gcd
        self.denominator //= gcd
        #return self.numerator, self.denominator
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
    
    def as_decimal(self):
        '''Evaluate fractions as decimal'''
        #print(round(self.numerator / self.denominator, 3))
        dec = self.numerator / self.denominator
        return round(dec, 3)

    #Add two Fraction() together 
    def __add__(self, other):
        '''Create a new fraction from addition: 
        x/y + a/b = xb/yb + ay/yb'''
        numerator2 = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        denominator2 = self.denominator * other.denominator
        # simpliy 
        return Fraction(numerator2, denominator2)
    
    def __sub__(self, other):
        '''Create a new fraction from subtraction : 
        x/y - a/b = xb/yb - ay/yb'''
        numerator2 = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        denominator2 = self.denominator * other.denominator
        # simpliy 
        return Fraction(numerator2, denominator2)
    
    def __mul__(self, other):
        '''Create a new fration from multiplication:
         x/y * a/b = xa/yb '''
        numerator2 = self.numerator * other.numerator
        denominator2 = self.denominator * other.denominator
        # simplify 
        return Fraction(numerator2, denominator2)
    
    def __truediv__(self, other):
        '''Create a new fractions from division:
        x/y / a/b = xb/ya'''
        numerator2 = self.numerator * other.denominator
        denominator2 = self.denominator * other.numerator
        # simplify 
        return Fraction(numerator2, denominator2)
    
    def __gt__(self, other):
        '''Evaluate which Fraction is greater than '''
        return self.numerator * other.denominator > other.numerator * self.denominator
     
    def __lt__(self, other):
        '''Evaluate which Fraction is less than'''
        return self.numerator * other.denominator < other.numerator * self.denominator
     
    def __eq__(self, other):
        '''Evaluate if Fraction()s are equal'''
        return self.numerator * other.denominator == other.numerator * self.denominator  

    def __str__(self):
        abs_numerator = abs(self.numerator)
        # numerator is less than denominator 
        if abs_numerator < self.denominator:
            return f"{self.numerator}/{self.denominator}"
        # greater but divisibale  
        elif self.numerator % self.denominator == 0:
            return f"{self.numerator // self.denominator}"
        # whole number with fraction
        else:
            whole_num = abs(self.numerator) // abs(self.denominator)
            remainder = abs(self.numerator) % abs(self.denominator)
            if self.numerator < 0:
                whole_num = -whole_num
            if whole_num == 0:
                return f"{self.numerator}/{self.denominator}"
            if self.numerator < 0 and whole_num != 0:
                return f"{whole_num}-{remainder}/{self.denominator}"
            return f"{whole_num}-{remainder}/{self.denominator}"
    