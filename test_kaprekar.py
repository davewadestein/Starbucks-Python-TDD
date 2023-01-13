import pytest
from mathy import kaprekar

# test_kaprekar.py

# What could go wrong?
# integer, but not 4 digits
# 1111
# '1234' strings maybe should be OK, if they can be converted to int
# other datatypes
# 6174...what if we start with the Kaprekar number?

# maybe we have the function return the first 4-digit computed number AND the number of iterations...?

def test_kaprekar_num(): # what if we send 6174 in, will it terminate?
    assert kaprekar(6174) == (6174, 1) # should equal itself and should only iterate once
    
    
def test_kaprekar_not_four_digits():
    with pytest.raises(ValueError): # should throw a ValueError exception
        kaprekar(123)
    
    
def test_kaprekar_all_same_digit(): # should throw a ValueError exception
    with pytest.raises(ValueError): 
        kaprekar(1111)
    

def test_kaprekar_string_number(): # should be OK to send in '1234'
    assert kaprekar('1234') == (3087, 3)
    
    
def test_kaprekar_weird_type():
    with pytest.raises(TypeError): # should throw a TypeError exception
        kaprekar([1, 2, 3, 4])