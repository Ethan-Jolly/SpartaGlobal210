import pytest
from string_calculator import *


def test_empty():
    assert string_calculator('') == '0'


def test_single_number():
    assert string_calculator('1') == '1'


def test_add():
    assert string_calculator('1,2') == '3'


def test_multiple_add():
    assert string_calculator('1,2,3,4,5') == '15'


def test_no_end_separator():
    assert type(string_calculator('1,2,')) == ValueError


@pytest.mark.parametrize('string, expected', [('//;\n1;3', '4'), ('//sep\n2sep5', '7')])
def test_user_assigned_separator(string, expected):
    assert string_calculator(string) == expected

