import pytest
from fizzbuzz import *


def test_FizzBuzz():
    assert type(FizzBuzz(5)) == str


def test_multiple_three():
    assert FizzBuzz(3) == "Fizz"


def test_multiple_five():
    assert FizzBuzz(5) == "Buzz"


def test_multiple_three_five():
    assert FizzBuzz(15) == "FizzBuzz"
