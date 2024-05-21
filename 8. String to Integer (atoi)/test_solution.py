from solution import solution_obj
from icecream import ic


def test1():
    text = "42"
    result = solution_obj.myAtoi(text)
    assert result == 42


def test2():
    text = "   -42"
    result = solution_obj.myAtoi(text)
    assert result == -42


def test3():
    text = "4193 with words"
    result = solution_obj.myAtoi(text)
    assert result == 4193


def test4():
    text = "words and 987"
    result = solution_obj.myAtoi(text)
    assert result == 0


def test5():
    text = "3.14159"
    result = solution_obj.myAtoi(text)
    assert result == 3


def test6():
    text = "-+12"
    result = solution_obj.myAtoi(text)
    assert result == 0


def test7():
    text = "21474836460"
    result = solution_obj.myAtoi(text)
    assert result == 2147483647


def test8():
    text = "  0000000000012345678"
    result = solution_obj.myAtoi(text)
    assert result == 12345678


def test9():
    text = "  -0012a42"
    result = solution_obj.myAtoi(text)
    assert result == -12

def test10():
    text = "0-1"
    result = solution_obj.myAtoi(text)
    assert result == 0

def test11():
    text = "-01324000"
    result = solution_obj.myAtoi(text)
    assert result == -1324000


    