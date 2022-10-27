from instructions import *
from registers import *
import pytest

def test_COPY_number():
    COPY(99, 'X') # copy 99 into X
    assert read_register('X') == 99
    
    
def test_COPY_register():
    write_register('X', 13)
    COPY('X', 'Y')
    assert read_register('Y') == 13
    

def test_COPY_invalid():
    with pytest.raises(ValueError):
        COPY(99, 'A') # should throw an exception 
        
        
def test_ADD_int():
    write_register('X', 0)
    ADD('X', 10, 'X')
    assert read_register('X') == 10
    

def test_ADD_reg():
    write_register('X', 10)
    ADD('X', 'X', 'X')
    assert read_register('X') == 20
    
    
def test_SUB_int():
    write_register('X', 0)
    SUB('X', 10, 'X')
    assert read_register('X') == -10
    

def test_SUB_reg():
    write_register('X', 10)
    SUB('X', 'X', 'X')
    assert read_register('X') == 0
    
    
def test_MUL_int():
    write_register('X', 10)
    MUL('X', 10, 'X')
    assert read_register('X') == 100
    

def test_MUL_reg():
    write_register('X', 10)
    MUL('X', 'X', 'X')
    assert read_register('X') == 100