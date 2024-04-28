from solution import solution_obj


def test1():
    x = 123
    result = solution_obj.reverse(x)
    assert result == 321


def test2():
    x = -123
    result = solution_obj.reverse(x)
    assert result == -321


def test3():
    x = 120
    result = solution_obj.reverse(x)
    assert result == 21


def test4():
    x = 1534236469
    result = solution_obj.reverse(x)
    assert result == 0
