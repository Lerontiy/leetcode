from main import Solution

obj = Solution()

def test1():
    input = 1
    assert obj.countVowelPermutation(input) == 5

def test2():
    input = 2
    assert obj.countVowelPermutation(input) == 10

def test3():
    input = 2
    assert obj.countVowelPermutation(input) == 10