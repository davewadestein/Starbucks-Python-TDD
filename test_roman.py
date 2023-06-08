import pytest
from roman import roman_to_arabic

def test_empty():
    assert roman_to_arabic('') == 0


def test_one_digit():
    assert roman_to_arabic('X') == 10


def test_descend():
    assert roman_to_arabic('MCLX') == 1160


def test_ascend():
    assert roman_to_arabic('MCMXCIX') == 1999


def test_lower_case():
    assert roman_to_arabic('x') == 10


def test_bad_digit():
    with pytest.raises(ValueError):
        assert roman_to_arabic('A')


