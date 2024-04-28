from icecream import ic


class Solution(object):
    def __init__(self):
        self.nums = [str(i) for i in range(1, 10)]

    def myAtoi(self, s: str):
        """
        :type s: str
        :rtype: int
        """

        ret_str = ""
        for i in s:
            ic(i)
            if len(ret_str) == 0:
                if i not in self.nums + [" ", "-", "+", "0"]:
                    return 0
                elif i in [" ", "0"]:
                    continue
                else:
                    ret_str += i
            else:
                if "+" in ret_str or "-" in ret_str:
                    if i in ["0"] + self.nums:
                        if "+" in ret_str:
                            ret_str = ret_str.replace("+", "")
                            ret_str += i
                        else:
                            ret_str += i
                    else:
                        return 0
                elif (i == "." and "." not in ret_str) or (i in self.nums + ["0"]):
                    ret_str += i

        try:
            ret_str = int(float(ret_str))
        except:  # noqa: E722
            ret_str = 0

        if ret_str < (-(2**31)):
            return -(2**31)
        elif ret_str > 2**31 - 1:
            return 2**31 - 1
        else:
            return ret_str


solution_obj = Solution()
