from registers import * # bad in production, but OK for testing
# from registers import read_register, write_register # or you could do this
import pytest

# The read function is pretty straightforward, but we could test it
# by putting something into a register and then ensuring it's there.
# Note that we could use write_register to put it in there, but then
# we have to worry about that function not working too. So let's
# write directly into the register (since this is a test, we can do that)

def test_read_register():
    registers['X'] = 123 # directly write to the register
    assert read_register('X') == 123 # use the function to view the value
    
    
def test_read_bad_register():
    # attempting to read from an invalid register should throw an exception
    with pytest.raises(ValueError):
        read_register('invalid')
        
        
def test_write_register():
    # we'll do the opposite here–we'll use the function to write, and then
    # peek in the dictionary to see if it did the write correctly
    x = read_register('X')
    write_register('Y', 345)
    assert registers['Y'] == 345
    assert registers['X'] == x # ensure we didn't change the other one
    
    
def test_write_bad_register():
    # attempting to write to an invalid register should throw an exception
    with pytest.raises(ValueError):
        write_register('invalid', 1)
        
        
def test_get_valid_int():
    assert get_valid_int('10') == 10
    

def test_get_invalid_int():
    # trying to parse an invalid int should raise an exception
    with pytest.raises(ValueError):
        get_valid_int('invalid')

        
def test_get_valid_int_out_of_range():
     with pytest.raises(ValueError):
        get_valid_int(12345) # out of range, so exception should be thrown
        
        
def test_get_operand_val_register():
    # given 'X' or any valid register name, should return its value
    assert get_operand_val('X') == read_register('X')
    

def test_get_operand_val_int():
    # given '10' or any string representing a valid int, should return its value
    # do we need this? Is it the same as get_valid_int test above?
    assert get_operand_val('10') == 10
