from solution import solution_obj
from icecream import ic


def test1():
    text = "PAYPALISHIRING"
    rows = 3
    result = solution_obj.convert(text, rows)
    ic(text, rows, result)
    assert result == "PAHNAPLSIIGYIR"


def test2():
    text = "PAYPALISHIRING"
    rows = 4
    result = solution_obj.convert(text, rows)
    ic(text, rows, result)
    assert result == "PINALSIGYAHRPI"


def test3():
    text = "A"
    rows = 1
    result = solution_obj.convert(text, rows)
    ic(text, rows, result)
    assert result == "A"


def test4():
    text = "AB"
    rows = 1
    result = solution_obj.convert(text, rows)
    ic(text, rows, result)
    assert result == "AB"


def test5():
    text = "ABC"
    rows = 1
    result = solution_obj.convert(text, rows)
    ic(text, rows, result)
    assert result == "ABC"


def test6():
    text = "пундик"
    rows = 2
    result = solution_obj.convert(text, rows)
    ic(text, rows, result)
    assert result == "пниудк"


def test7():
    text = "пундик"
    rows = 3
    result = solution_obj.convert(text, rows)
    ic(text, rows, result)
    assert result == "пиудкн"


# test1()
# test2()
# test3()
# test4()
# test5()
# test6()
# test7()
