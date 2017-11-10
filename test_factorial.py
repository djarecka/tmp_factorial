from my_code import my_factorial

def test_factorial():
    assert my_factorial(1) == 1
    assert my_factorial(5) == 120

def test_factorial_large():
    assert my_factorial(10000) > 0

import pytest

def test_factorial_negative():
    with pytest.raises(Exception):
       my_factorial(-10)
