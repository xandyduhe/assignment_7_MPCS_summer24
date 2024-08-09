import pytest
from problem2 import Fraction
import math 
    
def test_initialization():
    """Test fraction creation"""
    f1 = 0.625
    f = Fraction(5,8) 
    assert f.__str__() == "5/8"
    assert f.as_decimal() == 0.625
    # Add a test to not allow a denominator is 0
    try:
        f = Fraction(1,0)
    except ZeroDivisionError as err:
        print(f"Error: {err}")


def test_add():
    """Test the addition function"""
    f1 = Fraction(5,8) 
    f2 = Fraction(5,8) 

    add_them_up = f1 + f2
    assert add_them_up.__str__() != "10/8" 
    assert add_them_up.__str__() != "5/4" 
    assert add_them_up.__str__() == "1-1/4" 
    assert add_them_up.as_decimal() == 1.25
  
def test_subtract():
    """Test the subtraction function"""
    f1 = Fraction(1,2) 
    f2 = Fraction(2,1) 

    total = f1 - f2
    assert total.__str__() == "-1-1/2" 
    assert total.as_decimal() == -1.5


def test_multiply():
    """Test __mul__ function. Multiply two fractions together"""
    f1 = Fraction(5,8) 
    f2 = Fraction(2,1)
    f3 = f1 * f2
    assert f3.__str__() != "10/8"
    assert f3.as_decimal() == 1.25

def test_divide():
    """Test __truediv__ function. Divide one fraction by another """

    f1 = Fraction(5,8) 
    f2 = Fraction(1,1)
    f3 = f1 / f2
    assert f3.__str__() == "5/8"
    assert f3.as_decimal() == 0.625
    
    
def test_eq():
    """Test __eq__ fuction
     Compare if two fractions are equal """
    f1 = Fraction(5,8) 
    f2 = Fraction(5,8)
    f3 = Fraction(1,2)
    
    assert f1 == f2
    assert f1 != f3

def test_gt():
    """Test __gt__ fucntion 
    Compare two fractions using > and evaluate to True or False """

    f1 = Fraction(5,8) 
    f2 = Fraction(5,8)
    f3 = Fraction(1,2)
    
    assert (f1 > f2) == False 
    assert (f1 > f3) == True 
    assert (f3 > f2) == False 

    
def test_lt():
    """ Test __lt__ funtion 
    Compare two fractons using < and evaluate to True of False """

    f1 = Fraction(5,8) 
    f2 = Fraction(5,8)
    f3 = Fraction(1,2)
    
    assert (f1 < f2) == False 
    assert (f1 < f3) == False 
    assert (f3 < f2) == True 

