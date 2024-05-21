from icecream import ic


class Solution(object):
    def __init__(self):
        #self.nums = [str(i) for i in range(0, 10)]
        self.nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        ret_str = ""
        for i in s:
            ic(i, ret_str)
            if len(ret_str) == 0:
                if i not in self.nums and i not in [" ", "-", "+"]:
                    return 0
                elif i == " ":
                    continue
                else:
                    ret_str += i
            else:
                if "+" in ret_str or "-" in ret_str:
                    if len(ret_str) == 1 and i == "0":
                        continue
                    if i in self.nums:
                        ret_str += i
                    else:
                        break
                elif i in self.nums:
                    ret_str += i
                else:
                    break

        try:
            ret_str = int(ret_str)
        except:  # noqa: E722
            ret_str = 0

        if ret_str < (-(2**31)):
            return -(2**31)
        elif ret_str > 2**31 - 1:
            return 2**31 - 1
        else:
            return ret_str


solution_obj = Solution()
