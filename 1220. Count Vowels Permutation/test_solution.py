from main import Solution

obj = Solution()

def test():
    assert obj.countVowelPermutation(1) == 5
    assert obj.countVowelPermutation(2) == 10
    assert obj.countVowelPermutation(5) == 68
