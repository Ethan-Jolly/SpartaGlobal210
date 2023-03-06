import pytest
from simple_calc import *


def test_add():
    assert add(2, 2) == 4


def test_subtract():
    assert subtract(4, 2) == 2


def test_multiply():
    assert multiply(2, 2) == 4


def test_divide():
    assert divide(6, 2) == 3


# Parametrization
@pytest.mark.parametrize('num1, num2, expected', [(2, 2, 4), (5, 5, 10)])
def test_add_params(num1, num2, expected):
    assert add(num1, num2) == expected
