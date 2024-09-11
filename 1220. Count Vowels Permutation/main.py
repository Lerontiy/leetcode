class Solution:
    def countVowelPermutation(self, n: int) -> int:
        letters = {'a': ['e'], 'e': ['a', 'i'], 'i': ['a', 'e', 'o', 'u'], 'o': ['i', 'u'], 'u': ['a']}

        letters_count = [0 for _ in range(n)]
        string = ["" for _ in range(n)]
        res = 0
        i = 0

        while letters_count[0]<5 or i>0:
            if i==0:
                string[i] = list(letters)[letters_count[i]]
            else:
                string[i] = letters[string[i-1]][letters_count[i]]
        
            letters_count[i] += 1

            if i==n-1:
                res+=1

            if n>1 and i<n-1:
                i+=1

            while i>0 and letters_count[i]>=len(letters[string[i-1]]):
                i-=1

            if i<n-1:
                letters_count[i+1] = 0

        #print(res, n)
        return res

obj = Solution()    
def test():
    assert obj.countVowelPermutation(1) == 5
    assert obj.countVowelPermutation(2) == 10
    assert obj.countVowelPermutation(5) == 68
    obj.countVowelPermutation(25)

test()

